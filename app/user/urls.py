from django.urls import path

from app.user.views import UserSettingsView

urlpatterns = [
    path("user_settings/", UserSettingsView.as_view(), name="user_settings"),
]
