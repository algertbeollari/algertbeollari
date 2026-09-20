"""Controlled compliance assistant (v1, local-only).

Architecture, deliberately kept in one file for a v1:
  UI -> evidence-availability gate -> retrieval -> deterministic citation
  list -> optional Claude explanation (constrained to retrieved text) ->
  citation validation -> render.

Nothing here writes to any register, uploads files, or calls Claude when
no relevant evidence was retrieved. If you need those, that is a scope
change, not a bug fix, and needs its own governance sign-off per the
provider/deployment gate.
"""

import os

import streamlit as st
from anthropic import Anthropic

from retrieval import RetrievalIndex

MODEL = "claude-sonnet-5"

SYSTEM_PROMPT = """You are a compliance drafting assistant for a DFSA-regulated firm.

You will be given a question and a fixed set of source extracts, each tagged
with a source ID, title, authority and status. Rules, no exceptions:

1. Use ONLY the provided extracts. Do not add obligations, deadlines, or
   interpretations that are not stated in them.
2. Every substantive claim must cite a source ID in square brackets, e.g. [SAMPLE-001].
3. If the extracts do not answer the question, say plainly that the provided
   sources do not cover it, and do not guess.
4. Never present a superseded or draft source as current guidance without
   flagging its status.
5. Keep the answer concise and in professional British English.
"""


@st.cache_resource
def get_index() -> RetrievalIndex:
    idx = RetrievalIndex()
    idx.build()
    return idx


def get_client() -> Anthropic | None:
    key = os.environ.get("ANTHROPIC_API_KEY")
    if not key:
        return None
    return Anthropic(api_key=key)


def format_context(hits) -> str:
    blocks = []
    for score, chunk in hits:
        blocks.append(
            f"[{chunk.source_id}] {chunk.source_title} "
            f"(status: {chunk.source_status}, authority: {chunk.source_authority}, "
            f"effective: {chunk.effective_date})\n{chunk.text}"
        )
    return "\n\n---\n\n".join(blocks)


def cited_ids_present(answer: str, valid_ids: set[str]) -> bool:
    import re
    cited = set(re.findall(r"\[([A-Za-z0-9\-]+)\]", answer))
    if not cited:
        return False
    return cited.issubset(valid_ids)


st.set_page_config(page_title="Compliance Assistant (v1)", layout="wide")
st.title("Compliance Assistant — v1 (local, controlled)")
st.caption(
    "Retrieval-grounded only. Answers are limited to sources listed in manifest.json. "
    "This is a working v1, not an approved production system — see README.md."
)

index = get_index()

with st.sidebar:
    st.subheader("Source register")
    st.write(f"{len(index.chunks)} indexed chunks")
    if index.rejected:
        st.warning("Rejected sources:")
        for r in index.rejected:
            st.text(r)
    client = get_client()
    if client is None:
        st.error("ANTHROPIC_API_KEY not set. Explanation step disabled; "
                  "deterministic citation list will still work.")

query = st.text_input("Ask a question (answered only from indexed sources):")

if query:
    hits = index.search(query)

    if not hits:
        st.warning(
            "No sufficiently relevant evidence was found in the indexed sources "
            "for this question. Add or update sources in manifest.json, or "
            "rephrase the question. No answer has been generated."
        )
    else:
        st.subheader("Deterministic evidence")
        seen = set()
        valid_ids = set()
        for score, chunk in hits:
            valid_ids.add(chunk.source_id)
            if chunk.source_id not in seen:
                seen.add(chunk.source_id)
                flag = "" if chunk.source_status.lower() in ("current", "in-force", "approved") else " ⚠ NOT CURRENT"
                st.markdown(f"**[{chunk.source_id}] {chunk.source_title}** — {chunk.source_status}{flag}")

        client = get_client()
        if client is not None:
            context = format_context(hits)
            with st.spinner("Drafting explanation from retrieved extracts..."):
                response = client.messages.create(
                    model=MODEL,
                    max_tokens=1024,
                    system=SYSTEM_PROMPT,
                    messages=[{
                        "role": "user",
                        "content": f"Question: {query}\n\nSource extracts:\n\n{context}",
                    }],
                )
                answer = "".join(
                    block.text for block in response.content if block.type == "text"
                )

            if cited_ids_present(answer, valid_ids):
                st.subheader("Answer")
                st.write(answer)
            else:
                st.error(
                    "The model's draft cited a source not in the retrieved evidence, "
                    "or cited nothing. Falling back to evidence-only view above; "
                    "the drafted text has been discarded."
                )

        with st.expander("Why this answer? (raw retrieved extracts)"):
            for score, chunk in hits:
                st.text(f"score={score:.2f}  [{chunk.source_id}] chunk {chunk.chunk_index}")
                st.text(chunk.text)
                st.divider()
