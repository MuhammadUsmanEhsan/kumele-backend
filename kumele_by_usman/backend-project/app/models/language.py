from pydantic import BaseModel

class LanguagePreference(BaseModel):
    user_id: str
    language: str  # e.g., "en", "fr", "es", "ur"
