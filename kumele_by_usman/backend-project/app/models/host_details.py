from pydantic import BaseModel, EmailStr

class HostDetails(BaseModel):
    id: int
    name: str
    email: EmailStr
    phone: str
    organization: str
    bio: str
    profile_image_url: str
