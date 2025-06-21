
# 📘 Kumele API – Full Backend Documentation

This document contains **complete documentation** of the Kumele backend system. All APIs are **implemented**, **tested via Postman and Swagger**, and are **ready for frontend integration**.

---

## 🔗 Base URL

```
http://localhost:8000
```

- **Swagger UI**: [http://localhost:8000/docs](http://localhost:8000/docs)
- **Redoc UI**: [http://localhost:8000/redoc](http://localhost:8000/redoc)
- **Static assets**: `/static/...`

---

## ✅ Authentication & Account Management

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/auth/signup` | POST | Register with email/password |
| `/auth/login` | POST | Login with email/password |
| `/auth/passkey/register` | POST | Register with WebAuthn Passkey |
| `/auth/passkey/verify` | POST | Login using WebAuthn |
| `/auth/google-login` | POST | Google OAuth login |
| `/auth/signout` | POST | Logout |
| `/auth/remember-me` | POST | Enable 'Remember Me' token |
| `/auth/delete-account` | DELETE | Delete user account |
| `/auth/change-password` | POST | Change user password |
| `/auth/2fa/enable` | POST | Enable 2-Factor Auth |

---

## 👤 User Profile

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/user/profile/edit` | PUT | Update user profile |
| `/user/profile/hobbies` | PUT | Update hobbies |
| `/user/profile/followers` | GET | Get followers/following |
| `/user/language` | POST | Set preferred language |
| `/user/dark-mode` | POST | Toggle night mode |
| `/user/sound-notification` | POST | Toggle sound alerts |

---

## 🔓 WebAuthn

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/auth/passkey/register` | POST | Start registration |
| `/auth/passkey/verify` | POST | Verify credentials |

---

## 🌐 UI & System Toggles

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/intro/intro-video/skip` | POST | Skip intro video |
| `/intro/splash-toggle` | POST | Toggle splash screen |
| `/ui/icon-animation` | POST | Enable/disable animations |
| `/ui/swap-background` | POST | Change background |
| `/ui/swap-user-image` | POST | Change profile image |
| `/ui/swap-text` | POST | Update text content |

---

## 📧 Subscriber & Popups

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/subscribe` | POST | Subscribe to newsletter |
| `/popup/rate-event` | POST | Popup for event rating |
| `/popup/report-event` | POST | Report event popup |
| `/popup/follow-host` | POST | Follow host popup |

---

## 📜 Footer Pages

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/footer/about` | GET/POST | About Us content |
| `/footer/contact` | GET/POST | Contact page |
| `/footer/guidelines` | GET/POST | Community guidelines |
| `/footer/social` | GET/POST | Social media links |
| `/footer/terms` | GET/POST | Terms and conditions |
| `/footer/blog-links` | GET/POST | Blog & app store links |

---

## ✨ SEO

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/seo/meta` | POST | Page SEO meta data |

---

## 📅 Event Management

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/event/category` | POST | Add event category |
| `/event/image` | POST | Upload image |
| `/event/description` | POST | Add description |
| `/event/time-date` | POST | Set time & date |
| `/event/address` | POST | Add address |
| `/event/availability` | GET | Check availability |
| `/event/guests` | POST | Set guest count |
| `/event/card` | GET | Preview card |
| `/event/details` | GET | Event details |
| `/event/host-info` | GET | Host info |
| `/event/host-events` | GET | Other host events |
| `/event/share` | GET | Shareable QR |

---

## 📊 History & Stats

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/history/rewards` | GET | Reward popups |
| `/history/chart/pie` | GET | Pie chart |
| `/history/chart/bar` | GET | Bar chart |
| `/history/calendar` | GET | Calendar view |

---

## 💬 Chat System

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/chat` | POST/GET | Chat API |
| `/qr/event-info` | GET | QR Code for event |

---

## 🧠 Matching & Hobby Search

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/hobby/search` | POST | Filtered hobby search |
| `/hobby/matching` | POST | Match by hobby/location |

---

## 📝 Blog System

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/blog` | GET/POST | Add or fetch blogs |
| `/blog/search` | POST | Search blogs |
| `/blog/comment` | POST | Comment on blog |
| `/blog/add-players` | POST | Tag players in blog |

---

## 🎥 Video Platforms

Supports: **YouTube**, **Vimeo**, **Facebook Watch**, **Dailymotion**, **Tudi**, **Rumble**

---

## 💸 Payments & Crypto

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/payment/paypal` | POST | Pay for event |
| `/payment/stripe` | POST | Buy with Stripe |
| `/crypto/create-invoice` | POST | USDT/EURT via Plisio |

---

## 🔔 Notifications

Covers:

- Welcome messages
- Payment/Deletion confirmations
- Event Reminders
- Match & Blog notifications
- Birthday & Medal popups

---

## 🧪 Testing & Validation

- ✅ All APIs are **tested using Postman**
- ✅ All APIs are **visible via Swagger UI**
- ✅ All APIs are **ready for integration**

Use the provided `postman_collection.json` file and test via Swagger or Postman 
( I have tested all of these already )----> Tested by the Senior Developer Muhammad Usman.

---



For help or bugs: **Muhammad Usman** (Senior Dev) – Feel free to ping me anytime!

---

**🎉 All set – frontend can now fully integrate.** 💪
