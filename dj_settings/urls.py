from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include

from dj_settings.settings import DEBUG

urlpatterns = [
    path("", include("app.arc_dps_log.urls")),
    path("", include("app.uploader.urls")),
    path("", include("app.user.urls")),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if DEBUG:
    urlpatterns.append(path("bfi_uploder_admin/", admin.site.urls))
