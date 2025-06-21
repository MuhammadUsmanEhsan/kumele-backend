from fastapi import APIRouter, HTTPException
from app.models.delete_account import DeleteAccountRequest
from app.users import fake_users_db

router = APIRouter(prefix="/account", tags=["Delete Account"])

@router.post("/delete")
def delete_account(data: DeleteAccountRequest):
    user = fake_users_db.get(data.username)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    if user["password"] != data.password:
        raise HTTPException(status_code=401, detail="Incorrect password")

    del fake_users_db[data.username]
    return {"message": f"Account '{data.username}' deleted successfully."}
