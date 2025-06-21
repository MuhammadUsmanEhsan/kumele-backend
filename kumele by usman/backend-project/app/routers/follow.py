from fastapi import APIRouter, HTTPException
from app.models.follow import FollowRequest, UsernameRequest
from app.users import fake_users_db

router = APIRouter(prefix="/follow", tags=["Follow"])

@router.post("/add")
def follow_user(data: FollowRequest):
    follower = fake_users_db.get(data.follower)
    following = fake_users_db.get(data.following)

    if not follower or not following:
        raise HTTPException(status_code=404, detail="User not found")

    follower.setdefault("following", []).append(data.following)
    following.setdefault("followers", []).append(data.follower)

    return {"message": f"{data.follower} is now following {data.following}"}

@router.post("/followers")
def get_followers(data: UsernameRequest):
    user = fake_users_db.get(data.username)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return {"followers": user.get("followers", [])}

@router.post("/following")
def get_following(data: UsernameRequest):
    user = fake_users_db.get(data.username)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return {"following": user.get("following", [])}
