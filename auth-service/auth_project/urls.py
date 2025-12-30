from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

def api_info(request):
    return JsonResponse({
        "service": "Auth Service",
        "description": "User authentication and JWT token management",
        "endpoints": {
            "register": "/api/auth/register/",
            "login": "/api/auth/login/",
            "me": "/api/auth/me/",
            "admin": "/admin/"
        },
        "status": "✓ Running"
    })

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/auth/", include("accounts.urls")),
    path("", include("auth_frontend.urls")),
    path("", api_info),
]
