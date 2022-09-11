from django.urls import path

from app.core.views import LogsListView, UserSettingsView

urlpatterns = [
    path("", LogsListView.as_view(), name="logs_list"),
    path("user_settings/", UserSettingsView.as_view(), name="user_settings"),
]
