from models import AgentPersona


def demo_personas():
    items = []
    for i in range(1, 26):
        slug = f"demo_{i:02d}"
        items.append(AgentPersona(
            id=slug, name=f"Demo Participant {i:02d}",
            avatar_url=f"https://api.dicebear.com/9.x/shapes/svg?seed={slug}",
            linkedin_url=f"https://www.linkedin.com/in/{slug}",
            instagram_url=f"https://www.instagram.com/{slug}",
            needs=["Respectful communication", "Shared curiosity", "Compatible pace"],
            hobbies=["Design", "Technology", "Travel"] if i % 2 else ["Writing", "Music", "Cooking"],
            intellectual_style="Curious, collaborative, and direct.",
            quirks_and_habits=["Reflects before deciding", "Enjoys thoughtful questions"],
            dealbreakers=["Disrespect", "Dishonest communication"],
            vibe_summary="Synthetic demo profile for testing the agent dating workflow.",
            synthetic=True,
        ))
    return items

SEED_PERSONAS = demo_personas()
