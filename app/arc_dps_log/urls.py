from django.urls import path

from app.arc_dps_log.views import LogsListView

urlpatterns = [
    path("", LogsListView.as_view(), name="logs_list"),
]
