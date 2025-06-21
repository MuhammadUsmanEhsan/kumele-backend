from fastapi import APIRouter, HTTPException
from app.models.seo import PageSEO

router = APIRouter(prefix="/seo", tags=["SEO"])

# In-memory storage (simple dict) for SEO per page
seo_store = {}

@router.post("/set")
def set_seo(seo: PageSEO):
    seo_store[seo.page] = seo
    return {"message": f"SEO data set for page '{seo.page}'", "seo": seo}

@router.get("/get/{page}")
def get_seo(page: str):
    seo = seo_store.get(page)
    if not seo:
        raise HTTPException(status_code=404, detail="SEO data not found for this page")
    return seo
