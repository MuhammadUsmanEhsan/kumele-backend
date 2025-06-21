from fastapi import APIRouter, Query
from typing import List
from app.models.hobby_search import HobbySearchFilters

router = APIRouter(prefix="/hobby-search", tags=["Hobby Search"])

# Dummy hobby data for example
hobbies_db = [
    {"id": 1, "name": "Painting", "location": {"latitude": 40.7128, "longitude": -74.0060}, "paid": True, "age_min": 18, "age_max": 65},
    {"id": 2, "name": "Yoga", "location": {"latitude": 40.730610, "longitude": -73.935242}, "paid": False, "age_min": 16, "age_max": 70},
    {"id": 3, "name": "Gardening", "location": {"latitude": 40.741895, "longitude": -73.989308}, "paid": False, "age_min": 21, "age_max": 60},
]

def calculate_distance(loc1, loc2):
    # Simplified Euclidean distance for demo only
    return ((loc1["latitude"] - loc2["latitude"]) ** 2 + (loc1["longitude"] - loc2["longitude"]) ** 2) ** 0.5 * 111  # rough km

@router.post("/search", response_model=List[dict])
def search_hobbies(filters: HobbySearchFilters):
    loc = filters.change_location.dict() if filters.change_location else filters.current_location.dict()

    results = []
    for hobby in hobbies_db:
        dist = calculate_distance(hobby["location"], loc)
        if dist > filters.distance_km:
            continue
        if filters.paid_only and not hobby["paid"]:
            continue
        if filters.min_age and hobby["age_max"] < filters.min_age:
            continue
        if filters.max_age and hobby["age_min"] > filters.max_age:
            continue
        results.append(hobby)
    return results
