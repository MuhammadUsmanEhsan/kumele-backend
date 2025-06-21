from fastapi import APIRouter, HTTPException
from app.models.edit_profile import EditProfileRequest
from app.users import fake_users_db

router = APIRouter(prefix="/profile", tags=["Edit Profile"])

@router.put("/edit")
def edit_profile(data: EditProfileRequest):
    user = fake_users_db.get(data.username)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    if data.email:
        user["email"] = data.email
    if data.phone:
        user["phone"] = data.phone
    if data.password:
        user["password"] = data.password

    return {
        "message": "Profile updated successfully",
        "updated_user": user
    }
