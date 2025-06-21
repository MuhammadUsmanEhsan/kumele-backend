from pydantic import BaseModel

class ShareRequest(BaseModel):
    content_type: str  # e.g., "event", "profile"
    content_id: int    # ID of the content to share

class ShareResponse(BaseModel):
    share_url: str
