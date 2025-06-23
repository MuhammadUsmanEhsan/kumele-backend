from pydantic import BaseModel
from uuid import uuid4
from datetime import datetime, timedelta

fake_users_db = {}

class User(BaseModel):
    username: str
    email: str
    password: str
    phone: str
    referral_code: str
    referred_by: str | None = None
    events: list[dict] = []
    extra_info: dict = {}  # ← New field

def create_user(
    username: str,
    email: str,
    password: str,
    phone: str,
    referred_by: str | None = None,
    extra_info: dict = {}
) -> dict:
    if username in fake_users_db:
        raise ValueError("Username already exists")

    referral_code = str(uuid4())

    new_user = {
        "username": username,
        "email": email,
        "password": password,
        "phone": phone,
        "referral_code": referral_code,
        "referred_by": referred_by,
        "events": [
            {"type": "created", "timestamp": datetime.now() - timedelta(days=3)},
            {"type": "attended", "timestamp": datetime.now() - timedelta(days=2)},
            {"type": "created", "timestamp": datetime.now() - timedelta(days=10)},
            {"type": "attended", "timestamp": datetime.now() - timedelta(days=15)}
        ],
        "extra_info": extra_info  # ← Store additional data
    }

    fake_users_db[username] = new_user
    return new_user
