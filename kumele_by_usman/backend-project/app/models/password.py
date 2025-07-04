from pydantic import BaseModel

class PasswordUpdate(BaseModel):
    username: str
    old_password: str
    new_password: str
