from fastapi import APIRouter, HTTPException
from app.models.contact import ContactRequest

# In-memory store (replace with DB later if needed)
contact_messages = []

router = APIRouter(prefix="/contact", tags=["Contact"])

@router.post("/")
def submit_contact_form(data: ContactRequest):
    contact_messages.append({
        "name": data.name,
        "email": data.email,
        "message": data.message
    })
    return {"message": "Contact message received successfully"}
