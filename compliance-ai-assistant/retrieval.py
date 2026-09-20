"""Deterministic ingestion and retrieval layer.

Nothing here calls a model. Its only job is: read manifest.json, load only
the source files it declares, chunk them, and rank chunks against a query.
The chat layer (app.py) is responsible for deciding whether retrieved
evidence is sufficient before ever calling Claude.
"""

import json
import re
import hashlib
from dataclasses import dataclass, field
from pathlib import Path

from rank_bm25 import BM25Okapi

BASE_DIR = Path(__file__).parent
MANIFEST_PATH = BASE_DIR / "manifest.json"

ALLOWED_TYPES = {"public_regulation", "internal_policy", "synthetic"}
ALLOWED_CONTENT_LEVELS = {"public", "internal_non_personal"}


@dataclass
class SourceRecord:
    id: str
    title: str
    file: str
    type: str
    authority: str
    status: str
    effective_date: str
    permitted_content_level: str
    notes: str = ""
    sha256: str = field(default="")


@dataclass
class Chunk:
    source_id: str
    source_title: str
    source_status: str
    source_authority: str
    effective_date: str
    text: str
    chunk_index: int


STOPWORDS = {
    "a", "an", "and", "are", "as", "at", "be", "by", "for", "from", "has",
    "have", "how", "in", "is", "it", "its", "of", "on", "or", "our", "that",
    "the", "this", "to", "under", "was", "were", "what", "when", "where",
    "which", "who", "will", "with", "does", "do", "any", "must", "should",
    "can", "could",
}


def _tokenize(text: str) -> list[str]:
    return re.findall(r"[a-z0-9]+", text.lower())


def _significant_tokens(text: str) -> set[str]:
    return {t for t in _tokenize(text) if t not in STOPWORDS and len(t) > 2}


def load_manifest() -> list[SourceRecord]:
    if not MANIFEST_PATH.exists():
        return []
    data = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    records = []
    for entry in data.get("sources", []):
        records.append(SourceRecord(
            id=entry["id"],
            title=entry["title"],
            file=entry["file"],
            type=entry.get("type", "synthetic"),
            authority=entry.get("authority", "none"),
            status=entry.get("status", "unknown"),
            effective_date=entry.get("effective_date", "unknown"),
            permitted_content_level=entry.get("permitted_content_level", "public"),
            notes=entry.get("notes", ""),
        ))
    return records


def _chunk_text(text: str, max_chars: int = 800) -> list[str]:
    paragraphs = [p.strip() for p in text.split("\n\n") if p.strip()]
    chunks = []
    buf = ""
    for p in paragraphs:
        if len(buf) + len(p) + 2 <= max_chars:
            buf = f"{buf}\n\n{p}" if buf else p
        else:
            if buf:
                chunks.append(buf)
            buf = p
    if buf:
        chunks.append(buf)
    return chunks


class RetrievalIndex:
    """Rebuilt fresh on every app start. No hidden cross-run state."""

    def __init__(self):
        self.chunks: list[Chunk] = []
        self.rejected: list[str] = []
        self._bm25: BM25Okapi | None = None
        self._corpus_tokens: list[list[str]] = []

    def build(self) -> None:
        self.chunks = []
        self.rejected = []
        seen_ids = set()

        for record in load_manifest():
            if record.id in seen_ids:
                self.rejected.append(f"{record.id}: duplicate source ID, skipped")
                continue
            seen_ids.add(record.id)

            if record.type not in ALLOWED_TYPES:
                self.rejected.append(f"{record.id}: disallowed type '{record.type}', skipped")
                continue
            if record.permitted_content_level not in ALLOWED_CONTENT_LEVELS:
                self.rejected.append(
                    f"{record.id}: disallowed content level '{record.permitted_content_level}', skipped"
                )
                continue

            path = BASE_DIR / record.file
            try:
                resolved = path.resolve()
                if BASE_DIR.resolve() not in resolved.parents and resolved != BASE_DIR.resolve():
                    self.rejected.append(f"{record.id}: path escapes project root, skipped")
                    continue
            except OSError:
                self.rejected.append(f"{record.id}: invalid path, skipped")
                continue

            if not path.exists():
                self.rejected.append(f"{record.id}: file '{record.file}' not found, skipped")
                continue

            text = path.read_text(encoding="utf-8", errors="strict")
            record.sha256 = hashlib.sha256(text.encode("utf-8")).hexdigest()

            for i, chunk_text in enumerate(_chunk_text(text)):
                self.chunks.append(Chunk(
                    source_id=record.id,
                    source_title=record.title,
                    source_status=record.status,
                    source_authority=record.authority,
                    effective_date=record.effective_date,
                    text=chunk_text,
                    chunk_index=i,
                ))

        self._corpus_tokens = [_tokenize(c.text) for c in self.chunks]
        self._bm25 = BM25Okapi(self._corpus_tokens) if self._corpus_tokens else None

    def search(self, query: str, top_k: int = 6, min_overlap: int = 2, min_overlap_ratio: float = 0.25):
        """Relevance is decided by significant-token overlap with the query,
        not raw BM25 magnitude: BM25 scores are corpus-size dependent and can
        go negative for common terms in a small corpus, which would make a
        fixed score threshold an unreliable sufficiency gate. BM25 is used
        only to order candidates that already clear the overlap gate.
        """
        if self._bm25 is None:
            return []

        query_tokens = _significant_tokens(query)
        if not query_tokens:
            return []

        scores = self._bm25.get_scores(_tokenize(query))

        def status_rank(status: str) -> int:
            order = {"current": 0, "in-force": 0, "approved": 1, "draft": 2, "superseded": 3, "historical": 3}
            return order.get(status.lower(), 2)

        candidates = []
        for score, chunk in zip(scores, self.chunks):
            chunk_tokens = _significant_tokens(chunk.text)
            overlap = query_tokens & chunk_tokens
            if not overlap:
                continue
            ratio = len(overlap) / len(query_tokens)
            if len(overlap) >= min_overlap or ratio >= min_overlap_ratio:
                candidates.append((score, chunk))

        candidates.sort(key=lambda x: (status_rank(x[1].source_status), -x[0]))
        return candidates[:top_k]
