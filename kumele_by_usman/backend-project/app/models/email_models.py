from pydantic import BaseModel, EmailStr

class EmailRequest(BaseModel):
    email: EmailStr

class EmailVerification(BaseModel):
    email: EmailStr
    code: str
