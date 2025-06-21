from pydantic import BaseModel
from typing import Literal

class PaymentRequest(BaseModel):
    user_id: int
    amount: float
    method: Literal["card", "paypal", "stripe"]
    status: Literal["pending", "completed", "failed"] = "pending"
