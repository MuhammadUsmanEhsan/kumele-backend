from fastapi import APIRouter, HTTPException
from app.models.permissions_models import PermissionAssignment, PermissionQuery

router = APIRouter()

# Mock in-memory permissions store
permissions_db = {}

@router.post("/assign")
def assign_permissions(data: PermissionAssignment):
    permissions_db[data.username] = data.permissions
    return {"message": f"Permissions assigned to {data.username}", "permissions": data.permissions}

@router.post("/get")
def get_permissions(data: PermissionQuery):
    user_perms = permissions_db.get(data.username)
    if user_perms is None:
        raise HTTPException(status_code=404, detail="User not found")
    return {"username": data.username, "permissions": user_perms}
