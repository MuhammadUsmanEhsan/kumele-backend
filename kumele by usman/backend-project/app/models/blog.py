from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

class BlogPost(BaseModel):
    id: int = Field(default=None)
    title: str
    content: str
    authors: List[str]          # list of players/authors
    hobbies: Optional[List[str]] = []  # hobbies related to blog
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
