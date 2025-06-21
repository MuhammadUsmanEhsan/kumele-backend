from pydantic import BaseModel

class RememberMeRequest(BaseModel):
    username: str
    remember: bool
