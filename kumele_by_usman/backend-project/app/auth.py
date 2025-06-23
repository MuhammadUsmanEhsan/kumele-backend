from fastapi import APIRouter, HTTPException, Depends, status, Body
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel, EmailStr, Field, validator
from jose import JWTError, jwt
from datetime import date, datetime
from typing import Optional
import json

from app.auth_utils import (
    create_access_token, SECRET_KEY, ALGORITHM,
    send_2fa_code, check_2fa_code
)
from app.qrcode_utils import generate_qr_code
from app.rewards import calculate_user_rewards
from app.users import User, fake_users_db, create_user

# --- Conditional WebAuthn import ---
WEBAUTHN_AVAILABLE = False
try:
    from webauthn import (
        generate_registration_options,
        generate_authentication_options,
        options_to_json,
        verify_registration_response,
        verify_authentication_response,
        RegistrationCredential,
        AuthenticationCredential
    )
    from webauthn.helpers.structs import (
        PublicKeyCredentialRpEntity,
        PublicKeyCredentialUserEntity
    )
    WEBAUTHN_AVAILABLE = True
except ImportError:
    WEBAUTHN_AVAILABLE = False
# --------------------------------------

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")

# === Models ===
class LoginRequest(BaseModel):
    username: str
    password: str

class SignupRequest(BaseModel):
    name: str
    email: EmailStr
    gender: str = Field(..., regex="^(Male|Female|Non-Binary)$")
    dob_day: int
    dob_month: int
    dob_year: int
    password: str
    confirm_password: str
    referred_by: Optional[str] = None
    is_legal_adult: bool
    subscribe_newsletter: Optional[bool] = False
    agree_terms: bool
    captcha_verified: bool

    @validator("confirm_password")
    def passwords_match(cls, v, values):
        if "password" in values and v != values["password"]:
            raise ValueError("Passwords do not match")
        return v

    @validator("is_legal_adult")
    def must_be_legal_adult(cls, v):
        if not v:
            raise ValueError("You must confirm you are a legal adult")
        return v

    @validator("agree_terms")
    def must_agree_terms(cls, v):
        if not v:
            raise ValueError("You must agree to Terms & Conditions")
        return v

    @validator("captcha_verified")
    def check_captcha(cls, v):
        if not v:
            raise ValueError("CAPTCHA verification failed")
        return v

    @property
    def date_of_birth(self) -> date:
        return date(self.dob_year, self.dob_month, self.dob_day)

class TwoFARequest(BaseModel):
    phone: str

class TwoFACheck(BaseModel):
    phone: str
    code: str

class WebAuthnRegisterInit(BaseModel):
    username: str
    display_name: str

class WebAuthnRegisterFinish(BaseModel):
    username: str
    credential: dict

class WebAuthnLoginInit(BaseModel):
    username: str

class WebAuthnLoginFinish(BaseModel):
    username: str
    credential: dict

class QRLoginRequest(BaseModel):
    username: str
    password: str

class QRTokenValidation(BaseModel):
    token: str

# In-memory challenge storage
challenges: dict[str, str] = {}

# === Utility ===
def get_user(username: str):
    user_dict = fake_users_db.get(username)
    if user_dict:
        return User(**user_dict)

def verify_token(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if not username:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = get_user(username)
    if not user:
        raise credentials_exception
    return user

# === Basic Auth ===
@router.post("/login")
def login(data: LoginRequest):
    user = fake_users_db.get(data.username)
    if user and user["password"] == data.password:
        access_token = create_access_token(data={"sub": data.username})
        return {"access_token": access_token, "token_type": "bearer"}
    raise HTTPException(status_code=401, detail="Invalid credentials")

@router.post("/signup")
def signup(data: SignupRequest):
    today = date.today()
    dob = data.date_of_birth
    age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
    if age < 18:
        raise HTTPException(status_code=400, detail="You must be at least 18 years old to register.")

    try:
        new_user = create_user(
            username=data.email,
            email=data.email,
            password=data.password,
            referred_by=data.referred_by,
            phone=None,
            extra_info={
                "name": data.name,
                "gender": data.gender,
                "dob": str(dob),
                "subscribe_newsletter": data.subscribe_newsletter
            }
        )
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))

    return {
        "message": "Signup successful",
        "user": new_user,
        "note": f"Referred by: {data.referred_by}" if data.referred_by else "No referral used"
    }

@router.get("/protected")
def protected_route(current_user: User = Depends(verify_token)):
    return {"message": f"Hello {current_user.username}, this is a protected route!"}

# === 2FA SMS ===
@router.post("/2fa/send")
def send_2fa(data: TwoFARequest):
    try:
        sid = send_2fa_code(data.phone)
        return {"message": "2FA code sent", "sid": sid}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/2fa/verify")
def verify_2fa(data: TwoFACheck):
    try:
        verified = check_2fa_code(data.phone, data.code)
        if verified:
            return {"message": "2FA verification successful"}
        raise HTTPException(status_code=401, detail="Invalid or expired code")
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# === WebAuthn Endpoints ===
if WEBAUTHN_AVAILABLE:
    @router.post("/webauthn/register/init")
    def webauthn_register_init(data: WebAuthnRegisterInit):
        user_id = data.username.encode("utf-8")
        options = generate_registration_options(
            rp=PublicKeyCredentialRpEntity(id="localhost", name="Kumele App"),
            user=PublicKeyCredentialUserEntity(id=user_id, name=data.username, display_name=data.display_name)
        )
        challenges[data.username] = options.challenge
        return json.loads(options_to_json(options))

    @router.post("/webauthn/register/finish")
    def webauthn_register_finish(data: WebAuthnRegisterFinish):
        expected = challenges.get(data.username)
        if not expected:
            raise HTTPException(status_code=400, detail="No registration challenge found")
        credential = RegistrationCredential.parse_obj(data.credential)
        verification = verify_registration_response(
            credential=credential,
            expected_challenge=expected,
            expected_origin="http://localhost:8000",
            expected_rp_id="localhost"
        )
        fake_users_db[data.username]["credential_public_key"] = verification.credential_public_key
        return {"message": "WebAuthn registration successful"}

    @router.post("/webauthn/login/init")
    def webauthn_login_init(data: WebAuthnLoginInit):
        user = fake_users_db.get(data.username)
        if not user or "credential_public_key" not in user:
            raise HTTPException(status_code=404, detail="User has no WebAuthn credentials")
        options = generate_authentication_options(
            rp_id="localhost",
            allow_credentials=[{"id": user["credential_public_key"], "type": "public-key"}]
        )
        challenges[data.username] = options.challenge
        return json.loads(options_to_json(options))

    @router.post("/webauthn/login/finish")
    def webauthn_login_finish(data: WebAuthnLoginFinish):
        expected = challenges.get(data.username)
        user = fake_users_db.get(data.username)
        if not expected or not user:
            raise HTTPException(status_code=400, detail="Challenge or user not found")
        credential = AuthenticationCredential.parse_obj(data.credential)
        verification = verify_authentication_response(
            credential=credential,
            expected_challenge=expected,
            expected_origin="http://localhost:8000",
            expected_rp_id="localhost",
            credential_public_key=user["credential_public_key"]
        )
        access_token = create_access_token(data={"sub": data.username})
        return {"message": "Login successful", "access_token": access_token}

# === QR Code Login ===
@router.post("/qr/generate")
def generate_qr_login(data: QRLoginRequest):
    user = fake_users_db.get(data.username)
    if not user or user["password"] != data.password:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token(data={"sub": data.username})
    qr_image = generate_qr_code(token)

    return {
        "message": "QR code generated successfully",
        "token": token,
        "qr_image": qr_image
    }

@router.post("/qr/validate")
def validate_qr_token(data: QRTokenValidation):
    try:
        payload = jwt.decode(data.token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if username not in fake_users_db:
            raise HTTPException(status_code=401, detail="Invalid token user")
        return {
            "message": "QR login successful",
            "username": username
        }
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid or expired token")

# === Reward System ===
@router.post("/rewards")
def get_user_rewards(username: str = Body(...)):
    user = fake_users_db.get(username)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    event_logs = user.get("events", [])
    rewards = calculate_user_rewards(event_logs)
    return {"username": username, "rewards": rewards}
