from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(prefix="/guests", tags=["Guests"])

# Simple in-memory store for guest counts keyed by event_id (or user_id)
guest_counts = {}

class GuestCountRequest(BaseModel):
    event_id: str
    number_of_guests: int

@router.post("/set")
def set_guest_count(data: GuestCountRequest):
    if data.number_of_guests < 0:
        raise HTTPException(status_code=400, detail="Number of guests cannot be negative")
    guest_counts[data.event_id] = data.number_of_guests
    return {"message": "Guest count set successfully", "event_id": data.event_id, "number_of_guests": data.number_of_guests}

@router.get("/{event_id}")
def get_guest_count(event_id: str):
    count = guest_counts.get(event_id)
    if count is None:
        return {"message": "No guest count found for this event", "event_id": event_id, "number_of_guests": 0}
    return {"event_id": event_id, "number_of_guests": count}
