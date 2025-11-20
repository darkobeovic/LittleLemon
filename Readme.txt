Little Lemon Web Application – Back-End Capstone Project

This project implements:
- Menu API 
- Table Booking API
- Token-based authentication (DRF TokenAuth + Djoser)
- Full CRUD functionality for menu items and bookings
- MySQL backend integration (commented for compatibility; SQLite enabled by default)
- Unit tests for models and views
- Django-rendered HTML pages and static assets
- Full Git/GitHub version control

------------------------------------------------------
API ENDPOINTS FOR REVIEWERS
------------------------------------------------------

--- MENU API ---
GET    /restaurant/menu/items/
POST   /restaurant/menu/items/
GET    /restaurant/menu/items/<id>/
PUT    /restaurant/menu/items/<id>/
DELETE /restaurant/menu/items/<id>/

--- BOOKING API (REQUIRES AUTH TOKEN) ---
GET    /restaurant/booking/tables/
POST   /restaurant/booking/tables/
PUT    /restaurant/booking/tables/<id>/
DELETE /restaurant/booking/tables/<id>/

--- AUTHENTICATION ENDPOINTS ---
POST /restaurant/api-token-auth/        (DRF Token Auth)
POST /auth/users/                       (Djoser – register new user)
POST /auth/token/login/                 (Djoser – login, returns token)
POST /auth/token/logout/                (Djoser – logout)

--- STATIC HTML PAGE ---
GET /restaurant/

