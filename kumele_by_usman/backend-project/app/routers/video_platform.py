from fastapi import APIRouter, HTTPException
from typing import List
from app.models.video_platform import VideoPlatform

router = APIRouter(prefix="/video-platforms", tags=["Video Platforms"])

platform_db = {}
platform_id_counter = 1

# Initialize default platforms
def init_platforms():
    global platform_id_counter
    defaults = [
        {"name": "YouTube", "is_banned": False},
        {"name": "Dailymotion", "is_banned": False},
        {"name": "Vimeo", "is_banned": False},
        {"name": "Banned", "is_banned": True},
        {"name": "Tudi", "is_banned": False},
        {"name": "Facebook Watch", "is_banned": False},
        {"name": "Rumble", "is_banned": False},
    ]
    for p in defaults:
        global platform_id_counter
        platform_db[platform_id_counter] = VideoPlatform(id=platform_id_counter, **p)
        platform_id_counter += 1

init_platforms()

@router.get("/", response_model=List[VideoPlatform])
def get_platforms():
    return list(platform_db.values())

@router.get("/{platform_id}", response_model=VideoPlatform)
def get_platform(platform_id: int):
    platform = platform_db.get(platform_id)
    if not platform:
        raise HTTPException(status_code=404, detail="Platform not found")
    return platform

@router.post("/", response_model=VideoPlatform)
def add_platform(platform: VideoPlatform):
    global platform_id_counter
    platform.id = platform_id_counter
    platform_db[platform_id_counter] = platform
    platform_id_counter += 1
    return platform

@router.put("/{platform_id}", response_model=VideoPlatform)
def update_platform(platform_id: int, platform: VideoPlatform):
    if platform_id not in platform_db:
        raise HTTPException(status_code=404, detail="Platform not found")
    platform.id = platform_id
    platform_db[platform_id] = platform
    return platform

@router.delete("/{platform_id}")
def delete_platform(platform_id: int):
    if platform_id not in platform_db:
        raise HTTPException(status_code=404, detail="Platform not found")
    del platform_db[platform_id]
    return {"message": "Platform deleted"}
