from fastapi import APIRouter, HTTPException
from app.models.email import EmailUpdate

router = APIRouter(prefix="/email", tags=["Email"])

# In-memory database (can be replaced with real DB later)
email_db = {}

@router.post("/set")
def set_email(data: EmailUpdate):
    email_db[data.user_id] = data.email
    return {
        "message": f"Email set for user {data.user_id}",
        "email": data.email
    }

@router.get("/get/{user_id}")
def get_email(user_id: str):
    email = email_db.get(user_id)
    if not email:
        raise HTTPException(status_code=404, detail="Email not found for this user")
    return {"user_id": user_id, "email": email}
