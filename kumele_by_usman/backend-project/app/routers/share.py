from fastapi import APIRouter, HTTPException
from app.models.share import ShareRequest, ShareResponse

router = APIRouter(prefix="/share", tags=["Share"])

BASE_URL = "http://localhost:8000/shared"  # Replace with frontend/base URL in production

@router.post("/", response_model=ShareResponse)
def generate_share_link(data: ShareRequest):
    if data.content_type not in ["event", "profile"]:
        raise HTTPException(status_code=400, detail="Unsupported content type")

    share_url = f"{BASE_URL}/{data.content_type}/{data.content_id}"
    return ShareResponse(share_url=share_url)
