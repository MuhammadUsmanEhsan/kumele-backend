from fastapi import APIRouter, HTTPException
from app.models.user_image import UserImageSwap
from app.users import fake_users_db

router = APIRouter(prefix="/user-image", tags=["User Image Swap"])

@router.post("/swap")
def swap_user_image(data: UserImageSwap):
    user = fake_users_db.get(data.username)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    user["image_url"] = data.image_url
    return {"message": f"Image updated for user {data.username}", "image_url": data.image_url}

@router.get("/get/{username}")
def get_user_image(username: str):
    user = fake_users_db.get(username)
    if not user or "image_url" not in user:
        raise HTTPException(status_code=404, detail="User image not found")
    return {"username": username, "image_url": user["image_url"]}
