from fastapi import APIRouter, HTTPException
from app.models.nightmode import NightModeStatus

router = APIRouter(prefix="/nightmode", tags=["Night Mode"])

# In-memory store (replace with DB in real app)
night_mode_enabled = False

@router.get("/", response_model=NightModeStatus)
def get_night_mode_status():
    return {"enabled": night_mode_enabled}

@router.post("/toggle", response_model=NightModeStatus)
def toggle_night_mode(status: NightModeStatus):
    global night_mode_enabled
    night_mode_enabled = status.enabled
    return {"enabled": night_mode_enabled}
