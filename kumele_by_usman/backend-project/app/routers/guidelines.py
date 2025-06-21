from fastapi import APIRouter, HTTPException
from app.models.guidelines import Guideline

router = APIRouter(prefix="/guidelines", tags=["Guidelines"])

# In-memory store for demo purposes
guidelines_db: list[Guideline] = []

@router.get("/", response_model=list[Guideline])
def get_all_guidelines():
    return guidelines_db

@router.post("/")
def create_guideline(guideline: Guideline):
    for existing in guidelines_db:
        if existing.id == guideline.id:
            raise HTTPException(status_code=400, detail="Guideline with this ID already exists")
    guidelines_db.append(guideline)
    return {"message": "Guideline added successfully"}
