from fastapi import APIRouter, HTTPException
from typing import List

from app.models.business_ads import BusinessAdsResponse, Ad

router = APIRouter(prefix="/business-ads", tags=["Business Account Ads"])

# Dummy ads data for demo
ads_data = {
    1: [
        {
            "ad_id": 101,
            "title": "Summer Sale Campaign",
            "status": "active",
            "budget": 1000.00,
            "impressions": 15000,
            "clicks": 250,
            "start_date": "2025-06-01",
            "end_date": "2025-06-30"
        },
        {
            "ad_id": 102,
            "title": "New Product Launch",
            "status": "paused",
            "budget": 500.00,
            "impressions": 5000,
            "clicks": 80,
            "start_date": "2025-05-10",
            "end_date": "2025-05-20"
        }
    ]
}

@router.get("/{business_id}", response_model=BusinessAdsResponse)
def get_business_ads(business_id: int):
    if business_id not in ads_data:
        raise HTTPException(status_code=404, detail="Business ads not found")
    return BusinessAdsResponse(business_id=business_id, ads=ads_data[business_id])
