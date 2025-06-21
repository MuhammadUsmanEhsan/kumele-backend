from pydantic import BaseModel, EmailStr

class Subscriber(BaseModel):
    email: EmailStr

# In-memory storage (replace with DB in future)
subscribers = []
