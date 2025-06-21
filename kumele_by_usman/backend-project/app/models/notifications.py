from pydantic import BaseModel
from typing import Optional
from enum import Enum
from datetime import datetime


class NotificationType(str, Enum):
    NOTES = "Notes"
    MATCHED_EVENT = "Matched Events"
    CREATED_EVENT = "Created Events"
    JOIN_REQUEST = "Join Event"
    CANCELLED_EVENT = "Event Cancelled"
    BLOG_COMMENT = "Blog Comment"
    MEDAL = "Medal"
    BIRTHDAY = "Birthday"
    HOBBY_REMINDER = "Hobby Event Reminder"
    RATE_EVENT = "Rate Event"
    WELCOME = "Welcome"
    WHAT_TODO = "What would you like to do"
    NEW_BLOG = "New Blog"
    CONFIRMATION = "Confirmation"
    ADVERT = "Advert"
    MATCHED_NOTIFICATION = "Matched Notification"
    OTHER = "Other"


class Notification(BaseModel):
    id: int
    user_id: int
    type: NotificationType
    title: str
    message: Optional[str]
    read: bool = False
    timestamp: datetime
