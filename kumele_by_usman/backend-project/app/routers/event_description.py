from fastapi import APIRouter, HTTPException
from typing import Dict
from app.models.event_description import EventDescription

router = APIRouter(prefix="/event-description", tags=["Event Description"])

# In-memory store for simplicity (replace with DB in prod)
event_descriptions: Dict[int, str] = {}

@router.post("/", response_model=EventDescription)
def add_event_description(event_desc: EventDescription):
    event_descriptions[event_desc.event_id] = event_desc.description
    return event_desc

@router.get("/{event_id}", response_model=EventDescription)
def get_event_description(event_id: int):
    if event_id not in event_descriptions:
        raise HTTPException(status_code=404, detail="Event description not found")
    return EventDescription(event_id=event_id, description=event_descriptions[event_id])
