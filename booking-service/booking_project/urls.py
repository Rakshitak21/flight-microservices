<<<<<<< HEAD
from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse
from django_prometheus.exports import ExportToDjangoView
=======
"""
URL configuration for booking_project project.
"""
from django.contrib import admin
from django.urls import path, include

from django.http import JsonResponse
from django.conf import settings
>>>>>>> 9bebd6bc368c76f87785914b4ec6bf3487a1a978

def api_info(request):
    return JsonResponse({
        "service": "Booking Service",
<<<<<<< HEAD
        "status": "✓ Running",
        "metrics": "/metrics"
    })

urlpatterns = [
    # 🔥 PROMETHEUS — MUST BE FIRST
    path("metrics", ExportToDjangoView, name='prometheus-django-metrics'),

    # APIs
    path("api/", include("bookings.urls")),
    path("info/", api_info),

    # Admin
    path("admin/", admin.site.urls),

    # ❌ FRONTEND ABSOLUTELY LAST
    path("", include("booking_frontend.urls")),
]
=======
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

>>>>>>> 9bebd6bc368c76f87785914b4ec6bf3487a1a978
