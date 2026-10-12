from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from models import AgentPersona, DateSession, MatchRank, RawProfileData
from agent_engine import AgentEngine

app = FastAPI(title="Consent-Based Agent Dating Platform", version="1.0.0")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])
engine = AgentEngine()
DB_PERSONAS: dict[str, AgentPersona] = {}
DB_DATES: dict[str, DateSession] = {}

@app.get("/health")
def health():
    return {"status": "ok", "personas": len(DB_PERSONAS)}

@app.get("/api/personas", response_model=list[AgentPersona])
def get_personas():
    return list(DB_PERSONAS.values())

@app.get("/api/personas/{persona_id}", response_model=AgentPersona)
def get_persona(persona_id: str):
    if persona_id not in DB_PERSONAS: raise HTTPException(404, "Persona not found")
    return DB_PERSONAS[persona_id]

@app.post("/api/personas/create", response_model=AgentPersona)
def create_persona(raw: RawProfileData):
    try: persona = engine.analyze_profile(raw)
    except ValueError as exc: raise HTTPException(400, str(exc)) from exc
    DB_PERSONAS[persona.id] = persona
    return persona

@app.post("/api/date/simulate", response_model=DateSession)
def simulate_date(person_a_id: str, person_b_id: str):
    if person_a_id not in DB_PERSONAS or person_b_id not in DB_PERSONAS: raise HTTPException(404, "Persona not found")
    key = "_".join(sorted((person_a_id, person_b_id)))
    if key not in DB_DATES: DB_DATES[key] = engine.simulate_date(DB_PERSONAS[person_a_id], DB_PERSONAS[person_b_id])
    return DB_DATES[key]

@app.get("/api/rankings/{persona_id}", response_model=list[MatchRank])
def rankings(persona_id: str):
    if persona_id not in DB_PERSONAS: raise HTTPException(404, "Persona not found")
    result = []
    for other_id, other in DB_PERSONAS.items():
        if other_id == persona_id: continue
        session = engine.simulate_date(DB_PERSONAS[persona_id], other)
        result.append(MatchRank(target_person_id=persona_id, candidate_person_id=other_id, candidate_name=other.name, score=session.overall_compatibility, compatibility_reason=session.match_analysis, friction_point="Validate communication pace and boundaries directly."))
    return sorted(result, key=lambda x: x.score, reverse=True)
