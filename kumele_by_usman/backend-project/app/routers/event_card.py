from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

router = APIRouter(prefix="/event-card", tags=["Event Card"])

class EventCard(BaseModel):
    id: int
    title: str
    description: str
    image_url: str
    date: str
    location: str

# Dummy database (in-memory list)
event_cards_db: List[EventCard] = []

@router.post("/")
def create_event_card(event: EventCard):
    event_cards_db.append(event)
    return {"message": "Event card created", "event": event}

@router.get("/")
def get_all_event_cards():
    return {"events": event_cards_db}
