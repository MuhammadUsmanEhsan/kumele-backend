from pydantic import BaseModel

class Referral(BaseModel):
    username: str       # user who owns the referral code
    referral_code: str  # unique referral code
    referred_users: list[str] = []  # usernames of users referred
