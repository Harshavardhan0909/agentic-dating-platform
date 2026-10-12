from typing import List
from pydantic import BaseModel, Field, HttpUrl

class SourceRef(BaseModel):
    source: str
    url: HttpUrl
    evidence: str
    confidence: float = Field(ge=0, le=1)

class RawProfileData(BaseModel):
    name: str = Field(min_length=2, max_length=120)
    linkedin_url: HttpUrl
    instagram_url: HttpUrl
    headline: str = ""
    bio_summary: str = ""
    work_history: List[str] = Field(default_factory=list)
    instagram_captions: List[str] = Field(default_factory=list)
    tags_and_vibes: List[str] = Field(default_factory=list)
    sources: List[SourceRef] = Field(default_factory=list)

class AgentPersona(BaseModel):
    id: str
    name: str
    avatar_url: str = ""
    linkedin_url: HttpUrl
    instagram_url: HttpUrl
    needs: List[str] = Field(default_factory=list)
    hobbies: List[str] = Field(default_factory=list)
    intellectual_style: str = ""
    quirks_and_habits: List[str] = Field(default_factory=list)
    dealbreakers: List[str] = Field(default_factory=list)
    vibe_summary: str = ""
    sources: List[SourceRef] = Field(default_factory=list)
    synthetic: bool = True

class DateMessage(BaseModel):
    sender: str
    dialogue: str
    explanation: str = ""

class DateSession(BaseModel):
    person_a_id: str
    person_b_id: str
    transcript: List[DateMessage]
    chemistry_score: int = Field(ge=0, le=100)
    intellectual_score: int = Field(ge=0, le=100)
    lifestyle_score: int = Field(ge=0, le=100)
    overall_compatibility: int = Field(ge=0, le=100)
    match_analysis: str

class MatchRank(BaseModel):
    target_person_id: str
    candidate_person_id: str
    candidate_name: str
    score: int
    compatibility_reason: str
    friction_point: str
