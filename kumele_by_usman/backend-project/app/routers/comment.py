from fastapi import APIRouter, HTTPException, Depends
from datetime import datetime
from typing import List
from app.models.comment import Comment

router = APIRouter(prefix="/comment", tags=["Comment"])

comment_db = {}
comment_id_counter = 1

def fake_auth(username: str = None):
    # Simple stub: user must provide username query param or header to "authenticate"
    if not username:
        raise HTTPException(status_code=401, detail="Sign in required to comment")
    return username

@router.post("/")
def add_comment(comment: Comment, username: str = Depends(fake_auth)):
    global comment_id_counter
    comment.id = comment_id_counter
    comment.created_at = datetime.utcnow()
    comment.username = username
    comment_db[comment_id_counter] = comment
    comment_id_counter += 1
    return {"message": "Comment added", "comment": comment}

@router.get("/{blog_id}")
def get_comments(blog_id: int) -> List[Comment]:
    return [c for c in comment_db.values() if c.blog_id == blog_id]
