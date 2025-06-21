from fastapi import APIRouter, HTTPException
from app.models.edit_password import EditPasswordRequest
from app.users import fake_users_db

router = APIRouter(prefix="/user", tags=["Edit Password"])

@router.post("/change-password")
def change_password(data: EditPasswordRequest):
    user = fake_users_db.get(data.username)

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    if user["password"] != data.old_password:
        raise HTTPException(status_code=403, detail="Incorrect old password")

    user["password"] = data.new_password
    return {"message": "Password updated successfully"}
