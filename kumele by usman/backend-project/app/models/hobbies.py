from pydantic import BaseModel
from typing import List

class EditHobbiesRequest(BaseModel):
    username: str
    hobbies: List[str]
