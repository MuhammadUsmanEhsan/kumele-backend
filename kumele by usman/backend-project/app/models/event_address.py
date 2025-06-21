from pydantic import BaseModel

class EventAddress(BaseModel):
    event_id: int
    address_line1: str
    address_line2: str | None = None
    city: str
    state: str
    postal_code: str
    country: str
