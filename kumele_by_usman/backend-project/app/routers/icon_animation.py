from fastapi import APIRouter, HTTPException
from app.models.icon_animation import IconAnimation

router = APIRouter(prefix="/icon-animation", tags=["Icon Animation"])

# In-memory store for icon animations
icon_animations = {}

@router.post("/set")
def set_animation(config: IconAnimation):
    icon_animations[config.icon_name] = config
    return {"message": f"Animation set for '{config.icon_name}'", "config": config}

@router.get("/get/{icon_name}")
def get_animation(icon_name: str):
    if icon_name not in icon_animations:
        raise HTTPException(status_code=404, detail="No animation config found for this icon")
    return icon_animations[icon_name]
