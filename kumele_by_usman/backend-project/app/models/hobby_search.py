from pydantic import BaseModel
from typing import Optional

class Location(BaseModel):
    latitude: float
    longitude: float

class HobbySearchFilters(BaseModel):
    current_location: Location
    change_location: Optional[Location] = None  # user can override current location
    distance_km: Optional[int] = 10  # default 10 km radius
    min_age: Optional[int] = None
    max_age: Optional[int] = None
    paid_only: Optional[bool] = False  # True = paid hobbies only, False = all (including free)
