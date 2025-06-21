from fastapi import APIRouter, HTTPException
from app.models.passkey import PasskeyStatusRequest
from app.users import fake_users_db

router = APIRouter(prefix="/passkey", tags=["Passkey"])

@router.post("/update")
def update_passkey_status(data: PasskeyStatusRequest):
    user = fake_users_db.get(data.username)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    user["has_passkey"] = data.has_passkey
    return {"message": "Passkey status updated", "has_passkey": data.has_passkey}

@router.get("/status/{username}")
def get_passkey_status(username: str):
    user = fake_users_db.get(username)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    return {"has_passkey": user.get("has_passkey", False)}
