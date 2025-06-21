from pydantic import BaseModel
from typing import Optional

class EditProfileRequest(BaseModel):
    username: str
    email: Optional[str] = None
    phone: Optional[str] = None
    password: Optional[str] = None
