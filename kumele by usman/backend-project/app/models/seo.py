from pydantic import BaseModel, HttpUrl
from typing import Optional

class PageSEO(BaseModel):
    page: str               # e.g., "home", "about", "contact"
    title: str
    description: str
    keywords: Optional[str] = None  # comma separated keywords
    canonical_url: Optional[HttpUrl] = None
