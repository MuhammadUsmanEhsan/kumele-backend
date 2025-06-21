from pydantic import BaseModel

class DeleteAccountRequest(BaseModel):
    username: str
    password: str  # Optional: add password check if needed
