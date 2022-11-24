from django.urls import path

from app.arc_dps_log.views import LogsListView, sync_uploader_view, find_local_logs_view

app_name = "arc_dps_log"
urlpatterns = [
    path("", LogsListView.as_view(), name="logs_list"),
    path("sync_uploader", sync_uploader_view, name="sync_uploader"),
    path("find_local_logs", find_local_logs_view, name="find_local_logs"),
]
