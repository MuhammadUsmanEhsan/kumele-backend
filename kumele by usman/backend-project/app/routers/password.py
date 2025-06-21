from fastapi import APIRouter, HTTPException
from app.models.password import PasswordUpdate
from app.users import fake_users_db

router = APIRouter(prefix="/password", tags=["Password"])

@router.post("/update")
def update_password(data: PasswordUpdate):
    user = fake_users_db.get(data.username)
    
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    if user["password"] != data.old_password:
        raise HTTPException(status_code=401, detail="Old password is incorrect")

    user["password"] = data.new_password
    return {"message": "Password updated successfully"}
