from pydantic import BaseModel

class RewardPopup(BaseModel):
    id: int = None
    title: str
    message: str
    active: bool = True
