from pydantic import BaseModel

class TextSwap(BaseModel):
    component: str  # e.g., "homepage_banner", "footer_note"
    text: str
