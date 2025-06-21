from fastapi import APIRouter, HTTPException
from app.models.sound_notification import SoundNotificationRequest
from app.users import fake_users_db

router = APIRouter(prefix="/settings", tags=["Sound Notification"])

@router.post("/sound")
def update_sound_notification(data: SoundNotificationRequest):
    user = fake_users_db.get(data.username)

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    user["sound_notification"] = data.enabled
    return {
        "message": "Sound notification preference updated",
        "enabled": data.enabled
    }
