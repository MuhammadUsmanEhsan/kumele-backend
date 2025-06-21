# app/qrcode_utils.py

import pyqrcode
import png
from io import BytesIO
import base64

def generate_qr_code(data: str) -> str:
    qr = pyqrcode.create(data)
    buffer = BytesIO()
    qr.png(buffer, scale=5)
    base64_image = base64.b64encode(buffer.getvalue()).decode("utf-8")
    return f"data:image/png;base64,{base64_image}"
