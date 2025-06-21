from fastapi import APIRouter, HTTPException
from typing import List
from app.models.chat import EventPopup, ReviewBar, DaysLeft, ScannedGuest, ChatMessage, EventQRCode

router = APIRouter(prefix="/chat", tags=["Chat"])

# Mock DB dicts (replace with real DB later)
popups_db = []
review_db = {}
days_left_db = {}
scanned_list_db = []
chat_messages_db = []
qr_code_db = {}

# --- Popup Endpoints ---

@router.post("/popup/")
def handle_popup(popup: EventPopup):
    popups_db.append(popup)
    return {"message": f"Popup action '{popup.action}' recorded for event {popup.event_id}"}

# --- Review Bar ---

@router.get("/review-bar/{event_id}", response_model=ReviewBar)
def get_review_bar(event_id: int):
    # Dummy data for example
    data = review_db.get(event_id, {"average_rating": 4.5, "total_reviews": 120})
    return ReviewBar(event_id=event_id, **data)

# --- Days Left ---

@router.get("/days-left/{event_id}", response_model=DaysLeft)
def get_days_left(event_id: int):
    days = days_left_db.get(event_id, 7)  # default 7 days left
    return DaysLeft(event_id=event_id, days_left=days)

# --- Scanned List per Event ---

@router.get("/scanned-list/{event_id}", response_model=List[ScannedGuest])
def get_scanned_list(event_id: int):
    scanned_guests = [g for g in scanned_list_db if g.event_id == event_id]
    return scanned_guests

@router.post("/scan-guest/")
def scan_guest(scanned: ScannedGuest):
    scanned_list_db.append(scanned)
    return {"message": f"Guest {scanned.guest_id} scanned for event {scanned.event_id}"}

# --- Grayout Past Events ---

@router.get("/grayout-past-events", response_model=List[int])
def get_past_events():
    # Return list of event_ids that are past (dummy static list)
    past_events = [101, 102, 103]
    return past_events

# --- Chat Messages ---

@router.post("/message/")
def send_message(msg: ChatMessage):
    chat_messages_db.append(msg)
    return {"message": "Message sent"}

@router.get("/messages/{chat_id}", response_model=List[ChatMessage])
def get_messages(chat_id: int):
    messages = [m for m in chat_messages_db if m.chat_id == chat_id]
    return messages

# --- QR Code ---

@router.get("/qr-code/{event_id}", response_model=EventQRCode)
def get_qr_code(event_id: int):
    # Dummy data
    qr = qr_code_db.get(event_id)
    if not qr:
        qr = EventQRCode(
            event_id=event_id,
            qr_code_data=f"https://qrcode.example.com/event/{event_id}",
            event_address="123 Event St, City",
            host_info="Host: John Doe, Contact: 123-456-7890"
        )
        qr_code_db[event_id] = qr
    return qr
