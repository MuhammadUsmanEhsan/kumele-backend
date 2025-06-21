from datetime import datetime, timedelta
from jose import jwt
from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv()

# JWT config
SECRET_KEY = "secret-key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Twilio Authy config
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_SERVICE_SID = os.getenv("TWILIO_SERVICE_SID")

twilio_client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def send_2fa_code(phone_number: str) -> str:
    verification = twilio_client.verify \
        .services(TWILIO_SERVICE_SID) \
        .verifications \
        .create(to=phone_number, channel="sms")
    return verification.sid

def check_2fa_code(phone_number: str, code: str) -> bool:
    verification_check = twilio_client.verify \
        .services(TWILIO_SERVICE_SID) \
        .verification_checks \
        .create(to=phone_number, code=code)
    return verification_check.status == "approved"
