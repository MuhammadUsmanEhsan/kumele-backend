from fastapi import APIRouter, HTTPException
from typing import Dict
from app.models.event_time import EventTime

router = APIRouter(prefix="/event-time", tags=["Event Time"])

# In-memory store for simplicity (replace with DB in prod)
event_times: Dict[int, EventTime] = {}

@router.post("/", response_model=EventTime)
def add_event_time(event_time: EventTime):
    event_times[event_time.event_id] = event_time
    return event_time

@router.get("/{event_id}", response_model=EventTime)
def get_event_time(event_id: int):
    if event_id not in event_times:
        raise HTTPException(status_code=404, detail="Event time not found")
    return event_times[event_id]
