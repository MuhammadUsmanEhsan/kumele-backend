from fastapi import APIRouter, HTTPException
from google.oauth2 import id_token
from google.auth.transport import requests
from app.models.google_auth import GoogleAuthRequest
from app.users import fake_users_db

router = APIRouter(prefix="/google-auth", tags=["Google Auth"])

CLIENT_ID = "YOUR_GOOGLE_CLIENT_ID.apps.googleusercontent.com"  # Replace with your actual Google client ID

@router.post("/login")
def google_login(data: GoogleAuthRequest):
    try:
        # Verify the token
        idinfo = id_token.verify_oauth2_token(data.id_token, requests.Request(), CLIENT_ID)

        # Get user info from token payload
        userid = idinfo['sub']
        email = idinfo.get('email')
        name = idinfo.get('name', '')
        
        # Check if user exists or create
        user = None
        for u in fake_users_db.values():
            if u['email'] == email:
                user = u
                break
        
        if not user:
            # Create a new user with minimal info and random password (or empty)
            from uuid import uuid4
            username = email.split('@')[0]
            while username in fake_users_db:
                username += str(uuid4())[:4]

            user = {
                "username": username,
                "email": email,
                "password": "",  # No password since OAuth login
                "phone": "",
                "referral_code": str(uuid4()),
                "referred_by": None,
                "google_user_id": userid
            }
            fake_users_db[username] = user

        # Here you might create your access token (JWT)
        from app.auth_utils import create_access_token
        access_token = create_access_token(data={"sub": user["username"]})

        return {
            "message": "Google login/signup successful",
            "access_token": access_token,
            "token_type": "bearer",
            "user": user
        }

    except ValueError:
        raise HTTPException(status_code=401, detail="Invalid Google token")
