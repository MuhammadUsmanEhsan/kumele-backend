from pydantic import BaseModel

class EventImageMetadata(BaseModel):
    event_id: int
    description: str | None = None
