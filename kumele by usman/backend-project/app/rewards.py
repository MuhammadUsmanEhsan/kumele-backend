from datetime import datetime, timedelta

REWARD_TIERS = {
    "Bronze": {"count": 2, "discount": 2},
    "Silver": {"count": 3, "discount": 4},
    "Gold": {"count": 4, "discount": 8}
}

def calculate_user_rewards(event_logs: list[dict]) -> list[dict]:
    now = datetime.now()
    recent_events = [e for e in event_logs if e["timestamp"] >= now - timedelta(days=30)]

    created = sum(1 for e in recent_events if e["type"] == "created")
    attended = sum(1 for e in recent_events if e["type"] == "attended")
    total = max(created, attended)

    rewards = []
    for tier, details in REWARD_TIERS.items():
        if total >= details["count"]:
            multiplier = total // details["count"]
            for _ in range(multiplier):
                rewards.append({"tier": tier, "discount": details["discount"]})
    return rewards
