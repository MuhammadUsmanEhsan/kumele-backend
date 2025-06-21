from pydantic import BaseModel
from typing import List

class Event(BaseModel):
    event_id: int
    title: str
    description: str
    date: str
    time: str

class HostEventsResponse(BaseModel):
    host_id: int
    events: List[Event]
