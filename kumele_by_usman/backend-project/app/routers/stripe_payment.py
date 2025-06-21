from fastapi import APIRouter
from app.models.stripe_payment import StripePaymentRequest
import stripe

router = APIRouter(prefix="/stripe", tags=["Stripe"])

stripe.api_key = "sk_test_..."  # Replace with your key

@router.post("/create-payment")
def create_stripe_payment(data: StripePaymentRequest):
    try:
        intent = stripe.PaymentIntent.create(
            amount=int(data.amount * 100),
            currency=data.currency,
            metadata={"user_id": data.user_id},
            description=data.description
        )
        return {"client_secret": intent.client_secret}
    except Exception as e:
        return {"error": str(e)}
