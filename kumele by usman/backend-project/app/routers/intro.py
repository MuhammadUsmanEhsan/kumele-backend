from fastapi import APIRouter

router = APIRouter(prefix="/intro", tags=["Intro Video"])

# Temporary in-memory flags (you'll later connect to DB or user settings)
intro_data = {
    "video_url": "https://example.com/intro.mp4",
    "show_intro": True,
    "skipped": False
}

@router.get("/intro-video")
def get_intro_video():
    return {
        "video_url": intro_data["video_url"],
        "show_intro": intro_data["show_intro"]
    }

@router.post("/intro-video/skip")
def skip_intro_video():
    intro_data["skipped"] = True
    return {"message": "Intro video skipped"}

@router.get("/intro-video/status")
def intro_video_status():
    return {"skipped": intro_data["skipped"]}
