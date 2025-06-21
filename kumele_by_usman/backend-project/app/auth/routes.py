from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from app.schemas.user import UserCreate
from app.models.user import User
from app.db.session import get_db
import uuid

auth_router = APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@auth_router.post("/signup")
def signup(user: UserCreate, db: Session = Depends(get_db)):
    existing = db.query(User).filter(User.email == user.email).first()
    if existing:
        raise HTTPException(status_code=400, detail="Email already exists")

    hashed_pw = pwd_context.hash(user.password)
    new_user = User(
        id=str(uuid.uuid4()),
        email=user.email,
        hashed_password=hashed_pw
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message": "User created successfully", "user_id": new_user.id}
