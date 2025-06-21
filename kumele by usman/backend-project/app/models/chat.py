from pydantic import BaseModel
from typing import List, Optional

# Popup actions for events
class EventPopup(BaseModel):
    event_id: int
    action: str  # e.g., "rate", "report", "scan", "follow"
    user_id: int
    details: Optional[str] = None  # extra info like report reason, rating, etc.

# Review bar data
class ReviewBar(BaseModel):
    event_id: int
    average_rating: float
    total_reviews: int

# Days left until event
class DaysLeft(BaseModel):
    event_id: int
    days_left: int

# Scanned guest info per event
class ScannedGuest(BaseModel):
    event_id: int
    guest_id: int
    scanned_at: str  # ISO datetime string

# Chat message model
class ChatMessage(BaseModel):
    chat_id: int
    sender_id: int
    message: str
    timestamp: str  # ISO datetime string
    animated: Optional[bool] = False

# QR code info for event
class EventQRCode(BaseModel):
    event_id: int
    qr_code_data: str  # encoded QR code string or URL
    event_address: str
    host_info: str
