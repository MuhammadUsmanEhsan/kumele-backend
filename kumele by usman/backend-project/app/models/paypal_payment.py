from pydantic import BaseModel

class PayPalPaymentRequest(BaseModel):
    event_id: int
    user_id: int
    amount: float
    currency: str = "USD"
