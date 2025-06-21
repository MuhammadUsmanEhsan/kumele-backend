from fastapi import APIRouter, HTTPException
from app.models.swap_text import TextSwap

router = APIRouter(prefix="/text", tags=["Text Swap"])

# In-memory store for simplicity
text_store = {}

@router.post("/swap")
def swap_text(data: TextSwap):
    text_store[data.component] = data.text
    return {
        "message": f"Text updated for '{data.component}'",
        "component": data.component,
        "text": data.text
    }

@router.get("/get/{component}")
def get_text(component: str):
    text = text_store.get(component)
    if not text:
        raise HTTPException(status_code=404, detail="Text not found for component")
    return {"component": component, "text": text}
