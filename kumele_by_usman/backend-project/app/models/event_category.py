from pydantic import BaseModel

class EventCategory(BaseModel):
    id: int
    name: str
    description: str
