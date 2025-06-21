from fastapi import APIRouter, HTTPException
from typing import List
from app.models.other_events import Event, HostEventsResponse

router = APIRouter(prefix="/host-events", tags=["Other Events From Host"])

# Simulated in-memory DB
host_events_db: dict[int, List[Event]] = {
    1: [
        Event(event_id=101, title="Startup Talk", description="Talk on startups", date="2025-07-01", time="14:00"),
        Event(event_id=102, title="Tech Workshop", description="Hands-on session", date="2025-07-05", time="10:00")
    ],
    2: [
        Event(event_id=201, title="Music Night", description="Live music event", date="2025-07-10", time="19:00")
    ]
}

@router.get("/{host_id}", response_model=HostEventsResponse)
def get_events_by_host(host_id: int):
    events = host_events_db.get(host_id)
    if not events:
        raise HTTPException(status_code=404, detail="No events found for this host")
    return HostEventsResponse(host_id=host_id, events=events)
