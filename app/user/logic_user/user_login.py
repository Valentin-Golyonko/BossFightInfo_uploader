import base64

from app.core.logic_core.request_handler import RequestHandler
from app.core.utility_scripts.core_constants import CoreConstants
from app.uploader.uploader_constants import UploaderConstants
from app.user.logic_user.crud_user import CRUDUser


class UserLogin:
    @classmethod
    def bfi_auth_flow(cls, request) -> tuple[dict, str]:
        rq_post = request.POST
        auth_data, error_msg = cls.login_to_bfi(rq_post)
        if not auth_data:
            return {}, error_msg

        bfi_user_data, error_msg = cls.user_data_bfi(auth_data)
        if not bfi_user_data:
            return {}, error_msg

        dude_settings = bfi_user_data.get("data", {}).get("dude_settings", {})
        dude_id: int = dude_settings.get("id")

        if (user_obj := CRUDUser.find_dude(dude_id)) is None:
            if CRUDUser.multiple_users_count() > 0:
                return {}, CoreConstants.ONLY_ONE_USER

            new_user_obj = CRUDUser.create_dude(
                rq_post, auth_data, dude_settings, dude_id
            )

            if new_user_obj is None:
                return {}, CoreConstants.CREATE_USER_ERROR
        else:
            new_user_obj = CRUDUser.update_user(user_obj, dude_settings)

        if not CRUDUser.login_user(request, dude_id):
            return {}, CoreConstants.UPLOADER_LOGIN_FAIL

        out_data = {
            "username": new_user_obj.username,
            "dude_id": new_user_obj.dude_id,
            "is_email_confirmed": new_user_obj.is_email_confirmed,
            "gw2_account_name": new_user_obj.gw2_account_name,
        }
        return out_data, CoreConstants.OK

    @staticmethod
    def login_to_bfi(rq_post: dict) -> tuple[dict, str]:
        username = rq_post.get("username")
        password = rq_post.get("password")

        response = RequestHandler.rq_post(
            url=UploaderConstants.BFI_LOGIN_URL,
            json_data={
                "username": username,
                "password": password,
            },
        )
        if response is None:
            return {}, CoreConstants.CONNECTION_ERROR

        is_ok, rs_data = RequestHandler.rq_status_and_data(response)
        if not is_ok:
            return {}, rs_data.get("error_msg", CoreConstants.UPLOADER_ERROR)

        out_data = {
            "dude_id": rs_data.get("data", {}).get("dude_id"),
            "auth_str": base64.b64encode(
                f"{username}:{password}".encode("utf-8")
            ).decode("utf-8"),
        }
        return out_data, CoreConstants.OK

    @staticmethod
    def user_data_bfi(auth_data: dict) -> tuple[dict, str]:
        response = RequestHandler.rq_get(
            url=f"{UploaderConstants.BFI_DUDES_URL}/{auth_data.get('dude_id')}/",
            auth_str=auth_data.get("auth_str", ""),
        )
        if response is None:
            return {}, CoreConstants.CONNECTION_ERROR

        is_ok, rs_data = RequestHandler.rq_status_and_data(response)
        if not is_ok:
            return {}, rs_data.get("error_msg", CoreConstants.UPLOADER_ERROR)

        return rs_data.get("data", {}), CoreConstants.OK

    @staticmethod
    def default_user_data() -> dict:
        return {
            "username": CoreConstants.MDASH_SYMBOL,
            "dude_id": CoreConstants.MDASH_SYMBOL,
            "is_email_confirmed": CoreConstants.MDASH_SYMBOL,
            "gw2_account_name": CoreConstants.MDASH_SYMBOL,
        }
