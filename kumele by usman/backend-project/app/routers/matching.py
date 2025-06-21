from fastapi import APIRouter, HTTPException
from app.models.matching import MatchingRequest, UserProfile
from app.users import fake_users_db

router = APIRouter(prefix="/match", tags=["Matching"])

@router.post("/")
def find_matches(data: MatchingRequest):
    user = fake_users_db.get(data.username)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    user_hobbies = set(user.get("hobbies", []))
    user_age = user.get("age")
    user_location = user.get("location")

    if user_age is None or user_location is None:
        raise HTTPException(status_code=400, detail="User profile incomplete")

    matched_users = []
    for other_username, other_user in fake_users_db.items():
        if other_username == data.username:
            continue

        other_hobbies = set(other_user.get("hobbies", []))
        other_age = other_user.get("age")
        other_location = other_user.get("location")

        if not other_age or not other_location:
            continue

        shared_hobbies = user_hobbies.intersection(other_hobbies)
        age_diff = abs(user_age - other_age)
        same_location = user_location.lower() == other_location.lower()

        if shared_hobbies and age_diff <= 5 and same_location:
            matched_users.append({
                "username": other_user["username"],
                "age": other_user["age"],
                "location": other_user["location"],
                "hobbies": list(other_hobbies)
            })

    return {"matches": matched_users}
