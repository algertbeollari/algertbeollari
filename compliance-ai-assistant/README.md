# Compliance Assistant — v1 (local, controlled)

A retrieval-grounded assistant: it answers only from source extracts you have
explicitly authorised in `manifest.json`, and validates that Claude's
explanation cites only sources actually retrieved. It does not invent
obligations, deadlines, or approvals.

**Status: working v1, not an approved production system.** It has not been
through independent review, security testing, or a DPIA/RoPA — see
*Before any real deployment* below.

## What it does

1. You list authorised source files in `manifest.json` (id, title, type,
   authority, status, effective date, permitted content level).
2. On startup, `retrieval.py` loads only manifest-listed files, chunks them,
   and builds a BM25 keyword index — no embeddings, no external calls, fully
   deterministic and rebuilt fresh every run.
3. You ask a question in the Streamlit UI. If no chunk scores above the
   relevance threshold, the app says so and stops — it never calls Claude on
   an empty evidence base.
4. If evidence is found, the deterministic citation list (source ID, title,
   status) is shown first, independent of the model.
5. Claude is then asked to explain the answer using *only* the retrieved
   extracts, with mandatory `[SOURCE-ID]` citations.
6. The app checks every citation in Claude's answer against the IDs actually
   retrieved. If Claude cites anything else, or cites nothing, the drafted
   text is discarded and you only see the deterministic evidence list.
7. A "Why this answer?" panel shows the raw retrieved chunks and match
   scores for audit purposes.

## What it deliberately does not do (yet)

- No file upload or write-back to any register — read-only over
  manifest-listed sources.
- No multi-user auth — this is a single-user local tool.
- No persistent chat history or logging beyond the running Streamlit session.
- No embeddings/vector DB — BM25 keyword search only, which is transparent
  and auditable but will miss purely semantic matches. Upgrading to
  embeddings is a deliberate follow-on step, not done here.

## Setup

```bash
cd compliance-ai-assistant
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env   # then edit .env with your Firm-managed Anthropic API key
export $(grep -v '^#' .env | xargs)
streamlit run app.py
```

The app binds to `127.0.0.1` only (see `.streamlit/config.toml`) — it is not
reachable from the network as configured.

## Adding real sources — read this before adding anything

`sources/SAMPLE-001.md` is a placeholder. Replace it, but first classify
whatever you plan to add against the Firm's data classification scheme:

- **Permitted for this local v1:** public DFSA Rulebook module extracts,
  synthetic/test data, and your Firm's own approved non-personal internal
  policy Markdown (e.g. sanitised Compliance Manual sections).
- **Not permitted without a separate authorised environment and explicit
  scope:** Personal Data, client/KYC records, Client Assets evidence,
  SAR/STR material, Board-confidential papers, credentials, or anything
  classified Confidential/Restricted.

For each new source: add a `manifest.json` entry (`type` must be
`public_regulation`, `internal_policy`, or `synthetic`; `permitted_content_level`
must be `public` or `internal_non_personal`), then drop the file under
`sources/`. Files without a manifest entry are silently ignored. Files whose
manifest entry uses a disallowed type/level are rejected and listed in the
sidebar under "Rejected sources."

## Before any real deployment beyond your own machine

This v1 is deliberately local-only. Moving it further requires a governance
step, not just a config change:

- A Firm-managed (not personal) Anthropic account and API key, held server-side.
- A DPIA/RoPA and processor/transfer/retention review if any personal or
  client data will ever reach the model.
- Named system owner and MLRO/Compliance sign-off before go-live.
- Authentication, role separation, HTTPS, audit logging, and backup/recovery
  if more than one person will use it or it leaves your machine.
- Security testing (including prompt-injection testing against the source
  ingestion path) before it touches anything beyond public/synthetic sources.

Do not skip this step by quietly pointing `manifest.json` at client files or
by hosting the app on a shared server "for now."
