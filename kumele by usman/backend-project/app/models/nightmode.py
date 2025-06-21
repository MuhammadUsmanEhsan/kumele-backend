from pydantic import BaseModel

class NightModeStatus(BaseModel):
    enabled: bool
