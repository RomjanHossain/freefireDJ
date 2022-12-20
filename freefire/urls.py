from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from freefire import settings

admin.site.site_header = "Free Fire Admin"
admin.site.site_title = "Free Fire Admin Portal"
admin.site.index_title = "Welcome to Free Fire Admin Portal"
admin.site.site_url = "https://www.freefire.com.bd"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("landing.urls")),
    path("api/", include("api.urls")),
]

if settings.DEBUG:  # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
