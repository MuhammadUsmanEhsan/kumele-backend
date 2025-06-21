from pydantic import BaseModel

class VideoPlatform(BaseModel):
    id: int = None
    name: str
    is_banned: bool = False
