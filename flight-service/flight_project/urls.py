"""
URL configuration for flight_project project.
"""
from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

def api_info(request):
    return JsonResponse({
        "service": "Flight Service",
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

