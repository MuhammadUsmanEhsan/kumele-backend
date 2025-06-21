from fastapi import APIRouter
from app.models.signout import SignoutRequest

router = APIRouter(prefix="/auth", tags=["Signout"])

@router.post("/signout")
def signout(data: SignoutRequest):
    # In stateless JWT, actual signout is handled client-side (remove token from storage)
    # Optionally: log signout, store token blacklist, etc.
    return {"message": f"User '{data.username}' signed out successfully."}
