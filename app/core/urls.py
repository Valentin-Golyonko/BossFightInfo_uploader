from django.urls import path

from app.core.views import LogsListView

urlpatterns = [
    path("", LogsListView.as_view(), name="logs_list"),
]
