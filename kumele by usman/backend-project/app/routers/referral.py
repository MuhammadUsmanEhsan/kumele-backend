from fastapi import APIRouter, HTTPException
from app.models.referral import Referral

router = APIRouter(prefix="/referral", tags=["Referral"])

# Simple in-memory storage
referrals_db = {}

@router.post("/create")
def create_referral(referral: Referral):
    if referral.username in referrals_db:
        raise HTTPException(status_code=400, detail="Referral already exists for this user")
    referrals_db[referral.username] = referral
    return {"message": "Referral created", "referral": referral}

@router.get("/{username}")
def get_referral(username: str):
    referral = referrals_db.get(username)
    if not referral:
        raise HTTPException(status_code=404, detail="Referral not found")
    return referral
