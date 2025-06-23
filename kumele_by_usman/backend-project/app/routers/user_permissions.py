from fastapi import APIRouter, HTTPException
from app.models.permissions_models import PermissionUpdate

router = APIRouter()

permission_store = {}

@router.post("/save")
def save_user_permissions(data: PermissionUpdate):
    permission_store[data.username] = data.permissions
    return {
        "message": "Permissions saved",
        "username": data.username,
        "permissions": data.permissions
    }

@router.get("/get/{username}")
def get_user_permissions(username: str):
    permissions = permission_store.get(username)
    if not permissions:
        raise HTTPException(status_code=404, detail="No permissions found")
    return {"username": username, "permissions": permissions}
