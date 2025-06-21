import os
from fastapi import APIRouter, File, UploadFile, Form
from fastapi.responses import JSONResponse

router = APIRouter(prefix="/event-image", tags=["Event Image"])

UPLOAD_DIR = "uploads/event_images"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/upload")
async def upload_event_image(
    event_id: int = Form(...),
    description: str = Form(""),
    image: UploadFile = File(...)
):
    file_location = f"{UPLOAD_DIR}/{event_id}_{image.filename}"
    
    with open(file_location, "wb+") as file_object:
        file_object.write(await image.read())

    return {
        "message": "Image uploaded successfully",
        "file_path": file_location,
        "event_id": event_id,
        "description": description
    }
