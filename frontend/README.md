# Agentic Dating Platform Frontend

This branch contains the backend foundation. A frontend can call:

- `GET /health`
- `GET /api/personas`
- `POST /api/personas/create`
- `POST /api/date/simulate?person_a_id=...&person_b_id=...`
- `GET /api/rankings/{persona_id}`

The original pasted frontend was not published because it exposed private model reasoning and depended on an incomplete real-person profiling pipeline. Use a consent-based UI that displays only public explanations.
