from fastapi import APIRouter, HTTPException
from typing import Dict
from app.models.event_address import EventAddress

router = APIRouter(prefix="/event-address", tags=["Event Address"])

# In-memory store for simplicity
event_addresses: Dict[int, EventAddress] = {}

@router.post("/", response_model=EventAddress)
def add_event_address(event_address: EventAddress):
    event_addresses[event_address.event_id] = event_address
    return event_address

@router.get("/{event_id}", response_model=EventAddress)
def get_event_address(event_id: int):
    if event_id not in event_addresses:
        raise HTTPException(status_code=404, detail="Event address not found")
    return event_addresses[event_id]
