from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

def api_info(request):
    return JsonResponse({
        "service": "Auth Service",
<<<<<<< HEAD
        "status": "running"
    })

urlpatterns = [
    path("", include("django_prometheus.urls")),  # ✅ THIS ENABLES /metrics
    path("admin/", admin.site.urls),
    path("api/auth/", include("accounts.urls")),
=======
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
>>>>>>> 9bebd6bc368c76f87785914b4ec6bf3487a1a978
    path("", api_info),
]
