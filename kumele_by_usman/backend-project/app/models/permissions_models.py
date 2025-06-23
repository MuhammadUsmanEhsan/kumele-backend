from pydantic import BaseModel
from typing import List

class PermissionAssignment(BaseModel):
    username: str
    permissions: List[str]

class PermissionQuery(BaseModel):
    username: str
