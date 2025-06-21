from pydantic import BaseModel

class EventDetails(BaseModel):
    id: int
    title: str
    description: str
    organizer: str
    category: str
    date: str
    time: str
    address: str
    image_url: str
    price: float
    guests_allowed: int
    is_virtual: bool
