from pydantic import BaseModel

class EventDescription(BaseModel):
    event_id: int
    description: str
