from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

# Existing routers
from app.auth import router as auth
from app.routers.intro import router as intro_router
from app.routers.footer import router as footer_router
from app.routers.subscriber import router as subscriber_router
from app.routers import seo
from app.routers import icon_animation
from app.routers import swap_background 
from app.routers import user_image
from app.routers import swap_text
from app.routers import language 
from app.routers import email
from app.routers import password
from app.routers import remember_me
from app.routers import not_robot
from app.routers import passkey
from app.routers import google_auth
from app.routers import edit_profile
from app.routers import hobbies
from app.routers import follow
from app.routers import edit_password
from app.routers import sound_notification
from app.routers import contact
from app.routers import guidelines
from app.routers import payment
from app.routers import terms
from app.routers import nightmode
from app.routers import delete_account
from app.routers import signout
from app.routers import event_category
from app.routers import event_image
from fastapi.staticfiles import StaticFiles
from app.routers import paypal
from app.routers import event_description
from app.routers import event_time
from app.routers import event_address
from app.routers import user_availability
from app.routers import guests
from app.routers import preview
from app.routers import event_card
from app.routers import event_details
from app.routers import host_details
from app.routers import other_events
from app.routers import share
from app.routers import matching
from app.routers import animation
from app.routers import referral, blog
from app.routers import blog, comment
from app.routers import video_platform  # Add this import
from app.routers import reward_popup, pie_chart, bar_chart, calendar_year
from app.routers import chat
from app.routers import hobby_search
from app.routers import business_home
from app.routers import business_ads
from app.routers import notifications
from app.routers import stripe_payment, crypto_payment, paypal_payment

# Add other routers here as needed, e.g., SEO, splash, etc.

app = FastAPI(
    title="Kumele API",
    description="Backend for Kumele App with Auth, Referral, WebAuthn, QR login, Intro Video and more.",
    version="1.0.0"
)

# Mount static directory for serving frontend (e.g., WebAuthn test page)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Include routers
app.include_router(auth)
app.include_router(intro_router)
app.include_router(footer_router)
app.include_router(subscriber_router)
app.include_router(seo.router)
app.include_router(icon_animation.router)
app.include_router(swap_background.router)
app.include_router(user_image.router)
app.include_router(swap_text.router)
app.include_router(language.router)
app.include_router(email.router)
app.include_router(password.router)
app.include_router(remember_me.router)
app.include_router(not_robot.router)
app.include_router(passkey.router)
app.include_router(google_auth.router)
app.include_router(edit_profile.router)
app.include_router(hobbies.router)
app.include_router(follow.router)
app.include_router(edit_password.router)
app.include_router(sound_notification.router)
app.include_router(contact.router)
app.include_router(guidelines.router)
app.include_router(payment.router)
app.include_router(terms.router)
app.include_router(nightmode.router)
app.include_router(delete_account.router)
app.include_router(signout.router)
app.include_router(event_category.router)
app.include_router(event_image.router)
app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")
app.include_router(paypal.router)
app.include_router(event_description.router)
app.include_router(event_time.router)
app.include_router(event_address.router)
app.include_router(user_availability.router)
app.include_router(guests.router)
app.include_router(preview.router)
app.include_router(event_card.router)
app.include_router(event_details.router)
app.include_router(host_details.router)
app.include_router(other_events.router)
app.include_router(share.router)
app.include_router(matching.router)
app.include_router(animation.router)
app.include_router(referral.router)
app.include_router(blog.router)
app.include_router(comment.router)
app.include_router(video_platform.router)
app.include_router(reward_popup.router)
app.include_router(pie_chart.router)
app.include_router(bar_chart.router)
app.include_router(calendar_year.router)
app.include_router(chat.router)
app.include_router(hobby_search.router)
app.include_router(business_home.router)
app.include_router(business_ads.router)
app.include_router(notifications.router)
app.include_router(stripe_payment.router)
app.include_router(crypto_payment.router)
app.include_router(paypal_payment.router)

# Include additional routers as you build them

@app.get("/")
def root():
    return {"message": "API is working. Use /docs for Swagger UI."}
