from fastapi import APIRouter, HTTPException
from typing import List
from datetime import datetime

from app.models.notifications import Notification, NotificationType

router = APIRouter(prefix="/notifications", tags=["Notifications"])

# ✅ Mock data
notifications_db = [
    Notification(
        id=1,
        user_id=1,
        type=NotificationType.WELCOME,
        title="Welcome to Kumele 🎉",
        message="Let’s get started with finding events you’ll love.",
        timestamp=datetime.utcnow()
    ),
    Notification(
        id=2,
        user_id=1,
        type=NotificationType.MATCHED_EVENT,
        title="🎯 You’ve got a matched event!",
        message="Based on your hobbies and location.",
        timestamp=datetime.utcnow()
    )
]


@router.get("/{user_id}", response_model=List[Notification])
def get_user_notifications(user_id: int):
    return [n for n in notifications_db if n.user_id == user_id]


@router.post("/", response_model=Notification)
def create_notification(notification: Notification):
    notifications_db.append(notification)
    return notification
