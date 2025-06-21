from fastapi import APIRouter
from app.models.paypal_payment import PayPalPaymentRequest

router = APIRouter(prefix="/paypal", tags=["PayPal"])

@router.post("/pay")
def pay_with_paypal(data: PayPalPaymentRequest):
    # Placeholder response — your PayPal logic would be implemented here
    return {
        "message": f"Initiated PayPal payment for event {data.event_id}",
        "amount": data.amount,
        "currency": data.currency
    }
