from fastapi import APIRouter, HTTPException
from app.models.not_robot import RobotCheckRequest
from app.users import fake_users_db

router = APIRouter(prefix="/robot-check", tags=["Robot Check"])

@router.post("/verify")
def verify_robot_check(data: RobotCheckRequest):
    user = fake_users_db.get(data.username)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    user["is_human"] = data.is_human
    return {"message": "Human verification updated", "verified": data.is_human}

@router.get("/status/{username}")
def get_robot_status(username: str):
    user = fake_users_db.get(username)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    return {"is_human": user.get("is_human", False)}
