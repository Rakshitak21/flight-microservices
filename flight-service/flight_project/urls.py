<<<<<<< HEAD
=======
"""
URL configuration for flight_project project.
"""
>>>>>>> 9bebd6bc368c76f87785914b4ec6bf3487a1a978
from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

def api_info(request):
    return JsonResponse({
        "service": "Flight Service",
<<<<<<< HEAD
        "status": "✓ Running",
        "endpoints": {
            "api": "/api/",
            "metrics": "/metrics/",
            "admin": "/admin/"
        }
    })

urlpatterns = [
    path("", include("django_prometheus.urls")),  # /metrics
    path("admin/", admin.site.urls),
    path("api/", include("flights.urls")),
    path("", include("flight_frontend.urls")),
    path("info/", api_info),
]
=======
        "description": "Flight search and booking microservice",
        "endpoints": {
            "flights": "/api/flights/flights/",
            "search": "/api/flights/search/",
            "admin": "/admin/"
        },
        "status": "✓ Running with 13,047 flights loaded"
    })

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/flights/', include('flights.urls')),
    path('', include('flight_frontend.urls')),
    path('', api_info),
]

>>>>>>> 9bebd6bc368c76f87785914b4ec6bf3487a1a978
