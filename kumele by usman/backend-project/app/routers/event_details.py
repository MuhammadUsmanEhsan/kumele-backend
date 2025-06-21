from fastapi import APIRouter, HTTPException
from typing import List
from app.models.event_details import EventDetails

router = APIRouter(prefix="/event-details", tags=["Event Details"])

# Simulated DB
event_details_db: List[EventDetails] = []

@router.post("/")
def create_event(event: EventDetails):
    event_details_db.append(event)
    return {"message": "Event created", "event": event}

@router.get("/{event_id}")
def get_event(event_id: int):
    for event in event_details_db:
        if event.id == event_id:
            return event
    raise HTTPException(status_code=404, detail="Event not found")

@router.get("/")
def list_events():
    return {"events": event_details_db}
