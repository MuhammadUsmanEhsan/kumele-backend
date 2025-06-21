from pydantic import BaseModel

class UserImageSwap(BaseModel):
    username: str
    image_url: str  # New image URL
