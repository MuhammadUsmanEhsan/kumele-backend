from pydantic import BaseModel, HttpUrl

class FooterLinks(BaseModel):
    about_us: str
    contact_email: str
    blog_url: HttpUrl
    guidelines_url: HttpUrl
    android_app_url: HttpUrl
    ios_app_url: HttpUrl
    social_media_links: dict[str, HttpUrl]  # e.g. {"facebook": "...", "twitter": "..."}
