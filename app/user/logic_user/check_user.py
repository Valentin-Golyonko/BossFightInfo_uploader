import logging

from app.user.logic_user.crud_user import CRUDUser

logger = logging.getLogger(__name__)


class CheckUser:

    @staticmethod
    def check_user() -> tuple[bool, str]:
        user_obj = CRUDUser.get_uploader_user()
        if user_obj is None:
            logger.error(f"check_user(): no user for upload")
            return False, ""

        if not user_obj.is_email_confirmed:
            logger.error(
                f"check_user(): ! You must confirm your registration on the main web server !"
            )
            return False, ""

        if not user_obj.auth_str:
            logger.error(f"check_user(): ! wrong user credentials !")
            return False, ""

        return True, user_obj.auth_str
