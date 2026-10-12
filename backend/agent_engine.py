from __future__ import annotations
from typing import Dict
from urllib.parse import urlparse
from models import RawProfileData, AgentPersona

ALLOWED_HOSTS = {"linkedin.com", "www.linkedin.com", "instagram.com", "www.instagram.com"}

def validate_public_urls(raw: RawProfileData) -> None:
    for url in (raw.linkedin_url, raw.instagram_url):
        host = urlparse(str(url)).netloc.lower()
        if host not in ALLOWED_HOSTS:
            raise ValueError("Only LinkedIn and Instagram URLs are accepted")

def deterministic_persona(raw: RawProfileData) -> AgentPersona:
    validate_public_urls(raw)
    profile_id = "".join(ch.lower() if ch.isalnum() else "_" for ch in raw.name).strip("_")
    evidence = raw.bio_summary or raw.headline or "User-approved profile input"
    return AgentPersona(
        id=profile_id,
        name=raw.name,
        avatar_url=f"https://api.dicebear.com/9.x/shapes/svg?seed={profile_id}",
        linkedin_url=raw.linkedin_url,
        instagram_url=raw.instagram_url,
        needs=["Clear communication", "Mutual respect", "Compatible pace"],
        hobbies=raw.tags_and_vibes[:4] or ["Exploring interests from approved profile data"],
        intellectual_style=raw.headline or "Reflective and curious conversationalist.",
        quirks_and_habits=raw.work_history[:3] or ["Prefers evidence-backed profile attributes"],
        dealbreakers=["Disrespect", "Misrepresentation"],
        vibe_summary=evidence[:280],
        sources=raw.sources,
        synthetic=True,
    )

class AgentEngine:
    def analyze_profile(self, raw: RawProfileData) -> AgentPersona:
        return deterministic_persona(raw)

    def simulate_date(self, a: AgentPersona, b: AgentPersona):
        from models import DateSession, DateMessage
        shared = sorted(set(x.lower() for x in a.hobbies) & set(x.lower() for x in b.hobbies))
        score = min(95, 62 + len(shared) * 8)
        return DateSession(
            person_a_id=a.id, person_b_id=b.id,
            transcript=[
                DateMessage(sender=a.name, dialogue=f"What has been energising you lately?", explanation="Open-ended compatibility prompt."),
                DateMessage(sender=b.name, dialogue=f"I value curiosity and a thoughtful pace. What about you?", explanation="Values and communication check."),
                DateMessage(sender=a.name, dialogue="That sounds promising. What would make collaboration or a relationship feel sustainable?", explanation="Lifestyle and boundaries check."),
            ],
            chemistry_score=score,
            intellectual_score=min(95, score + 4),
            lifestyle_score=max(45, score - 3),
            overall_compatibility=score,
            match_analysis="The simulated conversation shows respectful curiosity and a plausible communication fit. Scores are illustrative, not claims about either person.",
        )
