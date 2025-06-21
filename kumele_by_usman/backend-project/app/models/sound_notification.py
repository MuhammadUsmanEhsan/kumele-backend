from pydantic import BaseModel

class SoundNotificationRequest(BaseModel):
    username: str
    enabled: bool
