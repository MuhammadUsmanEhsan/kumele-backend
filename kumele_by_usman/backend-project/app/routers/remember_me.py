from fastapi import APIRouter, HTTPException
from app.models.remember_me import RememberMeRequest
from app.users import fake_users_db

router = APIRouter(prefix="/remember", tags=["Remember Me"])

@router.post("/set")
def set_remember_me(data: RememberMeRequest):
    user = fake_users_db.get(data.username)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    user["remember_me"] = data.remember
    return {
        "message": f"Remember Me set to {data.remember} for user {data.username}"
    }

@router.get("/status/{username}")
def get_remember_me_status(username: str):
    user = fake_users_db.get(username)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return {
        "remember_me": user.get("remember_me", False)
    }
