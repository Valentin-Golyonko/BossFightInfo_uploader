import logging

from django.contrib.auth import login, authenticate

from app.user.models import CustomUser

logger = logging.getLogger(__name__)


class CRUDUser:
    @staticmethod
    def find_dude(dude_id: int) -> CustomUser | None:
        try:
            return CustomUser.objects.get(dude_id=dude_id)
        except CustomUser.DoesNotExist:
            pass
        except CustomUser.MultipleObjectsReturned:
            logger.error(f"find_dude(): MultipleObjectsReturned; {dude_id = }")
        except Exception as ex:
            logger.error(f"find_dude(): get Ex; {dude_id = }; {ex = }")
        return None

    @staticmethod
    def create_dude(
            rq_post: dict, auth_data: dict, dude_settings: dict, dude_id: int
    ) -> CustomUser | None:
        try:
            user_obj = CustomUser(
                username=rq_post.get("username"),
                auth_str=auth_data.get("auth_str"),
                dude_id=dude_id,
                is_email_confirmed=dude_settings.get("is_email_confirmed"),
                gw2_account_name=dude_settings.get("gw2_account_name"),
            )
            user_obj.set_password(rq_post.get("password"))
            user_obj.save()
        except Exception as ex:
            logger.error(f"create_dude(): get Ex; {dude_id = }; {ex = }")
            return None
        else:
            return user_obj

    @staticmethod
    def update_user(user_obj: CustomUser, dude_settings: dict) -> CustomUser | None:
        try:
            user_obj.is_email_confirmed = dude_settings.get("is_email_confirmed")
            user_obj.gw2_account_name = dude_settings.get("gw2_account_name")
            user_obj.save()
        except Exception as ex:
            logger.error(f"update_user(): get Ex; {user_obj.dude_id = }; {ex = }")
            return None
        else:
            return user_obj

    @staticmethod
    def login_user(request, dude_id: int) -> bool:
        try:
            auth_dude = authenticate(
                request,
                username=request.POST.get("username"),
                password=request.POST.get("password"),
            )
            if auth_dude is not None:
                login(request, auth_dude)
                return True
        except Exception as ex:
            logger.error(f"login_user() Ex; {dude_id = }; {ex = }")
        return False

    @staticmethod
    def multiple_users_count() -> int:
        try:
            return CustomUser.objects.filter(dude_id__gt=0).count()
        except Exception as ex:
            logger.error(f"multiple_users_exists(): count Ex; {ex = }")
            return 0
