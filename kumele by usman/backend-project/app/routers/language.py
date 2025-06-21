from fastapi import APIRouter, HTTPException
from app.models.language import LanguagePreference

router = APIRouter(prefix="/language", tags=["Language"])

# Simple in-memory store
language_db = {}

@router.post("/set")
def set_language(pref: LanguagePreference):
    language_db[pref.user_id] = pref.language
    return {
        "message": f"Language set to '{pref.language}' for user {pref.user_id}",
        "language": pref.language
    }

@router.get("/get/{user_id}")
def get_language(user_id: str):
    lang = language_db.get(user_id)
    if not lang:
        raise HTTPException(status_code=404, detail="Language not set for this user")
    return {"user_id": user_id, "language": lang}
