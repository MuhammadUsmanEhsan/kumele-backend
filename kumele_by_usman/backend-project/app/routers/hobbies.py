from fastapi import APIRouter, HTTPException
from app.models.hobbies import EditHobbiesRequest
from app.users import fake_users_db

router = APIRouter(prefix="/profile", tags=["Hobbies"])

@router.put("/edit-hobbies")
def edit_hobbies(data: EditHobbiesRequest):
    user = fake_users_db.get(data.username)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    user["hobbies"] = data.hobbies
    return {
        "message": "Hobbies updated successfully",
        "hobbies": user["hobbies"]
    }
