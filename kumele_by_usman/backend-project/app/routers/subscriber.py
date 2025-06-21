from fastapi import APIRouter, HTTPException
from app.models.subscriber import Subscriber, subscribers

router = APIRouter(prefix="/subscriber", tags=["subscriber"])

@router.post("/subscribe")
def subscribe(subscriber: Subscriber):
    if subscriber.email in [s.email for s in subscribers]:
        raise HTTPException(status_code=400, detail="Email already subscribed")
    subscribers.append(subscriber)
    return {"message": "Subscription successful"}

@router.get("/list")
def list_subscribers():
    return subscribers
