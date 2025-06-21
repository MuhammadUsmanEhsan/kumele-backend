from fastapi import APIRouter, HTTPException
from app.models.animation import AnimationConfig

router = APIRouter(prefix="/animations", tags=["Animations"])

# In-memory storage (replace with DB in production)
animations_db = {}

@router.post("/")
def set_animation(config: AnimationConfig):
    animations_db[config.component] = config
    return {"message": f"Animation for '{config.component}' saved successfully."}

@router.get("/{component}")
def get_animation(component: str):
    config = animations_db.get(component)
    if not config:
        raise HTTPException(status_code=404, detail="Animation not found for this component")
    return config
