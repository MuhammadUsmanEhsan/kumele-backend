from pydantic import BaseModel
from typing import Optional

class AnimationConfig(BaseModel):
    component: str            # e.g., "icon", "background", "button"
    animation_type: str       # e.g., "bounce", "fade", "slide"
    enabled: bool = True
    duration_ms: Optional[int] = 500  # optional duration in milliseconds
