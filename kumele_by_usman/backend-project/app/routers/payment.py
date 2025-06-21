from fastapi import APIRouter, HTTPException
from app.models.payment import PaymentRequest

router = APIRouter(prefix="/payments", tags=["Payments"])

# In-memory DB
payments_db: list[PaymentRequest] = []

@router.post("/")
def create_payment(payment: PaymentRequest):
    payments_db.append(payment)
    return {"message": "Payment initiated", "payment": payment}

@router.get("/")
def list_payments():
    return payments_db
