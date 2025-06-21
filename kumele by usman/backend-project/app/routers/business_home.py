from fastapi import APIRouter, HTTPException

from app.models.business_home import BusinessAccountHome

router = APIRouter(prefix="/business-home", tags=["Business Account Home"])

# Dummy data (in real app, fetch from DB)
business_data = {
    1: {
        "business_id": 1,
        "business_name": "Usman’s Store",
        "total_revenue": 12500.75,
        "total_customers": 150,
        "active_campaigns": 3,
        "new_messages": 5,
        "notifications": 2
    }
}

@router.get("/{business_id}", response_model=BusinessAccountHome)
def get_business_home(business_id: int):
    if business_id not in business_data:
        raise HTTPException(status_code=404, detail="Business not found")
    return business_data[business_id]
