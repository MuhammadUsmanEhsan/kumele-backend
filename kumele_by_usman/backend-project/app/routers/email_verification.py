from fastapi import APIRouter, HTTPException
from random import randint
from app.models.email_models import EmailRequest, EmailVerification

router = APIRouter()

verification_codes = {}

@router.post("/send-code")
def send_email_code(data: EmailRequest):
    code = str(randint(100000, 999999))
    verification_codes[data.email] = code
    return {"message": "Verification code sent (mocked)", "code": code}

@router.post("/verify-code")
def verify_email_code(data: EmailVerification):
    expected_code = verification_codes.get(data.email)
    if not expected_code:
        raise HTTPException(status_code=404, detail="No code sent to this email")
    if data.code != expected_code:
        raise HTTPException(status_code=400, detail="Incorrect code")
    return {"message": "Email verified"}
