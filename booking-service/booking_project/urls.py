"""
URL configuration for booking_project project.
"""
from django.contrib import admin
from django.urls import path, include

from django.http import JsonResponse
from django.conf import settings

def api_info(request):
    return JsonResponse({
        "service": "Booking Service",
        "description": "Flight booking and reservation management",
        "endpoints": {
            "bookings": "/api/bookings/bookings/",
            "create": "/api/bookings/create/",
            "admin": "/admin/"
        },
        "status": "✓ Running"
    })

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/bookings/', include('bookings.urls')),
    path('', include('booking_frontend.urls')),
    path('', api_info),
]


from django.conf import settings
from django.conf.urls.static import static
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

