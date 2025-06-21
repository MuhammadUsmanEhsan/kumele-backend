from fastapi import APIRouter, HTTPException, Query
from typing import List, Optional
from datetime import datetime
from app.models.blog import BlogPost

router = APIRouter(prefix="/blog", tags=["Blog"])

blog_db = {}
blog_id_counter = 1

@router.post("/")
def add_blog_post(post: BlogPost):
    global blog_id_counter
    post.id = blog_id_counter
    post.created_at = datetime.utcnow()
    blog_db[blog_id_counter] = post
    blog_id_counter += 1
    return {"message": "Blog post added", "post": post}

@router.get("/")
def get_all_blogs(
    search: Optional[str] = Query(None, description="Search term for title or content"),
    hobby: Optional[str] = Query(None, description="Filter by hobby")
) -> List[BlogPost]:
    results = list(blog_db.values())
    if search:
        results = [
            b for b in results if search.lower() in b.title.lower() or search.lower() in b.content.lower()
        ]
    if hobby:
        results = [
            b for b in results if hobby.lower() in (h.lower() for h in b.hobbies or [])
        ]
    return results

@router.get("/{blog_id}")
def get_blog(blog_id: int):
    blog = blog_db.get(blog_id)
    if not blog:
        raise HTTPException(status_code=404, detail="Blog post not found")
    return blog
