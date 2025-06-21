from fastapi import APIRouter, HTTPException
from app.models.swap_background import BackgroundConfig

router = APIRouter(prefix="/background", tags=["Swap Background"])

# In-memory store
background_settings = {}

@router.post("/set")
def set_background(config: BackgroundConfig):
    background_settings[config.page_name] = config
    return {"message": f"Background set for '{config.page_name}'", "config": config}

@router.get("/get/{page_name}")
def get_background(page_name: str):
    if page_name not in background_settings:
        raise HTTPException(status_code=404, detail="No background config found for this page")
    return background_settings[page_name]
