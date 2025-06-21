from pydantic import BaseModel
from typing import Optional

class BusinessAccountHome(BaseModel):
    business_id: int
    business_name: str
    total_revenue: Optional[float] = 0.0
    total_customers: Optional[int] = 0
    active_campaigns: Optional[int] = 0
    new_messages: Optional[int] = 0
    notifications: Optional[int] = 0
