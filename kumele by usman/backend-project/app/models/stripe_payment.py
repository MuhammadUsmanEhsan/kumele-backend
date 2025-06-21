from pydantic import BaseModel


class StripePaymentRequest(BaseModel):
    user_id: int
    amount: float
    currency: str = "usd"
    description: str
