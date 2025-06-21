from pydantic import BaseModel

class EditPasswordRequest(BaseModel):
    username: str
    old_password: str
    new_password: str
