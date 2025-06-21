from pydantic import BaseModel


class CryptoPaymentRequest(BaseModel):
    user_id: int
    amount: float
    currency: str  # e.g., "USDT", "EURT"
    order_name: str
