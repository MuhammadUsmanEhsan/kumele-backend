from pydantic import BaseModel

class IconAnimation(BaseModel):
    icon_name: str           # e.g., "event", "home", "profile"
    animation_type: str      # e.g., "bounce", "spin", "fade"
    enabled: bool
