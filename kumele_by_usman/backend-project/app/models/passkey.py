from pydantic import BaseModel

class PasskeyStatusRequest(BaseModel):
    username: str
    has_passkey: bool
