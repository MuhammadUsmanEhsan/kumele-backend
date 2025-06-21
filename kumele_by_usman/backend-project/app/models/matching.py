from pydantic import BaseModel
from typing import List

class MatchingRequest(BaseModel):
    username: str  # The user requesting matches

class UserProfile(BaseModel):
    username: str
    age: int
    location: str
    hobbies: List[str]
