from django.urls import path

from app.uploader.views import upload_log_view

app_name = "uploader"
urlpatterns = [
    path("upload_log/<int:id>/", upload_log_view, name="upload_log"),
]
