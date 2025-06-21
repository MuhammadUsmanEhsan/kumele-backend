from pydantic import BaseModel

class BackgroundConfig(BaseModel):
    page_name: str            # e.g., "home", "events", "profile"
    background_url: str       # e.g., https://example.com/bg1.jpg
    enabled: bool
