from pydantic import BaseModel

class SignoutRequest(BaseModel):
    username: str
    token: str  # optional for logging, debugging or blacklist logic
