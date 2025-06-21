from pydantic import BaseModel
from typing import List, Optional

class Ad(BaseModel):
    ad_id: int
    title: str
    status: str  # e.g. "active", "paused", "ended"
    budget: float
    impressions: Optional[int] = 0
    clicks: Optional[int] = 0
    start_date: str  # ISO date string
    end_date: Optional[str] = None  # ISO date string or null

class BusinessAdsResponse(BaseModel):
    business_id: int
    ads: List[Ad]
