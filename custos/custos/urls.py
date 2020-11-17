from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("users/", include("users.urls")),
    path("lists/", include("lists.urls")),
    path("", include("home.urls")),
    # oauth urls
    path("oauth", include("social_django.urls", namespace="social")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
