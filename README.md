# Agentic Dating Platform

A consent-based agent dating simulator using synthetic or explicitly consenting profiles.

## Safety scope

- Uses 25 synthetic/demo profiles by default.
- Accepts user-approved profile inputs only.
- Stores source citations and uncertainty labels.
- Exposes public match explanations, not hidden model reasoning.
- Simulates agent-to-agent conversations; it does not contact people or send messages.

## Planned stack

- FastAPI + Pydantic backend
- Next.js + TypeScript frontend
- OpenAI-compatible structured generation
- PostgreSQL/pgvector-ready persistence seam
- Playwright adapter for approved, user-authorized pages only

## Run

See `backend/README.md` and `frontend/README.md`. The repository is an implementation starter and requires environment configuration before deployment.
