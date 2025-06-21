from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/preview", tags=["Preview"])

class PreviewRequest(BaseModel):
    title: str
    description: str
    date: str | None = None  # optional date string
    image_url: str | None = None

@router.post("/")
def preview_content(data: PreviewRequest):
    # Just return the data back, maybe process/format as needed before final save
    return {
        "message": "Preview generated successfully",
        "preview": {
            "title": data.title,
            "description": data.description,
            "date": data.date,
            "image_url": data.image_url
        }
    }
