from pydantic import BaseModel, EmailStr

class EmailUpdate(BaseModel):
    user_id: str
    email: EmailStr
