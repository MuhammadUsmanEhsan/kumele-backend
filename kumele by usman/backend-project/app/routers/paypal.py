import httpx
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import os

router = APIRouter(prefix="/paypal", tags=["PayPal"])

# Replace with your own sandbox credentials or use .env variables
PAYPAL_CLIENT_ID = os.getenv("PAYPAL_CLIENT_ID", "YOUR_PAYPAL_CLIENT_ID")
PAYPAL_CLIENT_SECRET = os.getenv("PAYPAL_CLIENT_SECRET", "YOUR_PAYPAL_CLIENT_SECRET")
PAYPAL_API_BASE = "https://api-m.sandbox.paypal.com"

class CreateOrderRequest(BaseModel):
    amount: float
    currency: str = "USD"

# 🔐 Get Access Token
async def get_access_token():
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{PAYPAL_API_BASE}/v1/oauth2/token",
            data={"grant_type": "client_credentials"},
            auth=(PAYPAL_CLIENT_ID, PAYPAL_CLIENT_SECRET)
        )
    if response.status_code != 200:
        raise HTTPException(status_code=500, detail="Failed to authenticate with PayPal")
    return response.json()["access_token"]

# ✅ Create Order
@router.post("/create-order")
async def create_order(req: CreateOrderRequest):
    access_token = await get_access_token()
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    order_payload = {
        "intent": "CAPTURE",
        "purchase_units": [{
            "amount": {
                "currency_code": req.currency,
                "value": str(req.amount)
            }
        }]
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{PAYPAL_API_BASE}/v2/checkout/orders",
            json=order_payload,
            headers=headers
        )
    if response.status_code != 201:
        raise HTTPException(status_code=500, detail="Failed to create PayPal order")

    return response.json()

# ✅ Capture Order
@router.post("/capture-order/{order_id}")
async def capture_order(order_id: str):
    access_token = await get_access_token()
    headers = {"Authorization": f"Bearer {access_token}"}
    
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{PAYPAL_API_BASE}/v2/checkout/orders/{order_id}/capture",
            headers=headers
        )
    if response.status_code != 201:
        raise HTTPException(status_code=500, detail="Failed to capture PayPal order")
    
    return response.json()
