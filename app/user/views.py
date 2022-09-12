from http import HTTPStatus

from django.shortcuts import render
from django.views.generic import TemplateView

from app.user.logic_user.user_login import UserLogin


class UserSettingsView(TemplateView):
    template_name = "user_settings.html"

    def get(self, request, *args, **kwargs):
        if request.user.id is None:
            user_data = UserLogin.default_user_data()
        else:
            user_data = {
                "username": request.user.username,
                "dude_id": request.user.dude_id,
                "is_email_confirmed": request.user.is_email_confirmed,
                "gw2_account_name": request.user.gw2_account_name,
            }
        return render(request, self.template_name, {"user_data": user_data, "detail": ''})

    def post(self, request, *args, **kwargs):
        user_data, error_msg = UserLogin.bfi_auth_flow(request)
        if not user_data:
            return render(
                request=request,
                template_name=self.template_name,
                context={"user_data": UserLogin.default_user_data(), "detail": error_msg},
                status=HTTPStatus.BAD_REQUEST,
            )
        return render(
            request=request,
            template_name=self.template_name,
            context={"user_data": user_data, "detail": None},
            status=HTTPStatus.OK,
        )
