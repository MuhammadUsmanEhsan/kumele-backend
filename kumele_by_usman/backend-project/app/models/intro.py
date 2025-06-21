from pydantic import BaseModel
from typing import Optional

class IntroVideo(BaseModel):
    video_url: str
    show_skip: bool = True  # frontend uses this to show/hide "Skip" button

# Temporary in-memory skip state (for testing; later can be DB)
user_intro_skips = {}
