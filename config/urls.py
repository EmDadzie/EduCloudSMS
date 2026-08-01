from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

import config.admin_site

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("dashboard/", include("dashboard.urls")),
    path("students/", include("students.urls")),
    path("teachers/", include("teachers.urls")),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )