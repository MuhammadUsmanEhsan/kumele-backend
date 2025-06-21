from fastapi import APIRouter
from app.models.footer import FooterLinks

router = APIRouter(prefix="/footer", tags=["Footer"])

# Sample static footer info — you can extend or load dynamically later
footer_info = FooterLinks(
    about_us="Kumele is a platform for ...",
    contact_email="support@kumele.app",
    blog_url="https://blog.kumele.app",
    guidelines_url="https://kumele.app/guidelines",
    android_app_url="https://play.google.com/store/apps/details?id=com.kumele.app",
    ios_app_url="https://apps.apple.com/app/kumele/id123456789",
    social_media_links={
        "facebook": "https://facebook.com/kumele",
        "twitter": "https://twitter.com/kumele",
        "instagram": "https://instagram.com/kumele"
    }
)

@router.get("/", response_model=FooterLinks)
async def get_footer_info():
    return footer_info
