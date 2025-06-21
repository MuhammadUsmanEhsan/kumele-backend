from fastapi import APIRouter, HTTPException
from app.models.event_category import EventCategory

router = APIRouter(prefix="/event-category", tags=["Event Category"])

# In-memory DB
event_categories = []

@router.get("/")
def get_all_categories():
    return event_categories

@router.post("/")
def add_category(data: EventCategory):
    for cat in event_categories:
        if cat.id == data.id:
            raise HTTPException(status_code=400, detail="Category ID already exists")
    event_categories.append(data)
    return {"message": "Event category added successfully"}

@router.delete("/{category_id}")
def delete_category(category_id: int):
    global event_categories
    event_categories = [c for c in event_categories if c.id != category_id]
    return {"message": f"Category with ID {category_id} deleted"}
