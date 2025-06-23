from pydantic import BaseModel
from typing import Dict

class PermissionUpdate(BaseModel):
    username: str
    permissions: Dict[str, bool]
