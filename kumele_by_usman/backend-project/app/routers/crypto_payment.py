from fastapi import APIRouter
from app.models.crypto_payment import CryptoPaymentRequest
import requests
import os

router = APIRouter(prefix="/crypto", tags=["Crypto (Plisio)"])

PLISIO_API_KEY = "your_plisio_api_key_here"

@router.post("/create-invoice")
def create_crypto_invoice(data: CryptoPaymentRequest):
    url = "https://plisio.net/api/v1/invoices/new"
    payload = {
        "api_key": PLISIO_API_KEY,
        "amount": data.amount,
        "currency": data.currency,
        "order_name": data.order_name,
        "order_id": f"{data.user_id}_{data.order_name}"
    }
    response = requests.post(url, data=payload)
    return response.json()
