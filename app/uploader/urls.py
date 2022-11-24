from django.urls import path

from app.uploader.views import upload_logs_view

app_name = "uploader"
urlpatterns = [
    path("upload_logs", upload_logs_view, name="upload_logs"),
]
