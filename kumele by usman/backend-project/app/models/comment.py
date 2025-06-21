from pydantic import BaseModel
from datetime import datetime

class Comment(BaseModel):
    id: int = None
    blog_id: int
    username: str
    content: str
    created_at: datetime = None
