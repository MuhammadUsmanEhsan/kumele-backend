from fastapi import APIRouter

router = APIRouter(prefix="/user", tags=["User"])

# Assuming you already have fake_users_db from your users.py
from app.users import fake_users_db

@router.get("/check-availability/{username}")
def check_user_availability(username: str):
    if username in fake_users_db:
        return {"available": False, "message": "Username is already taken"}
    return {"available": True, "message": "Username is available"}
