"""
debug:
    from app.arc_dps_log.logic_logs.uploader_sync import UploaderSync
    UploaderSync.get_data_from_bfi()
run:
    python manage.py runscript app.arc_dps_log.logic_logs.uploader_sync
"""
import base64
import logging

from app.arc_dps_log.logic_logs.crud_local_log import CRUDLocalLog
from app.arc_dps_log.models import LocalLog
from app.core.logic_core.request_handler import RequestHandler
from app.core.utility_scripts.core_constants import CoreConstants
from app.core.utility_scripts.util_scripts import time_it
from app.uploader.uploader_constants import UploaderConstants
from app.user.logic_user.check_user import CheckUser
from app.user.logic_user.crud_user import CRUDUser
from app.user.logic_user.user_login import UserLogin

logger = logging.getLogger(__name__)


def run():
    UploaderSync.get_data_from_bfi()


class UploaderSync:
    @classmethod
    @time_it
    def get_data_from_bfi(cls) -> None:
        is_user_ok, auth_str, user_id = CheckUser.check_user(upload=False)
        if not is_user_ok:
            return None

        auth = base64.b64decode(auth_str).decode("utf-8").split(":")
        out_data, is_ok = UserLogin.login_to_bfi(
            {
                "username": auth[0],
                "password": auth[1],
            }
        )
        if is_ok != CoreConstants.OK:
            logger.error(f"recursion_uploader_sync(): login_to_bfi Error")
            return None

        is_sync_ok, results = cls.recursion_uploader_sync(
            url=UploaderConstants.BFI_UPLOADER_SYNC_URL,
            access_token=out_data.get("access_token"),
        )
        if not is_sync_ok:
            CRUDUser.update_sync(user_id, is_synced=False)
            return None
        elif not results:
            CRUDUser.update_sync(user_id, is_synced=True)
            return None

        logs_to_save = []
        count = 0
        is_synced = False

        for log_data in results:
            count += 1

            logs_to_save.append(
                LocalLog(
                    file_name=log_data.get("file_name"),
                    file_path=log_data.get("file_path"),
                    file_time=log_data.get("file_time"),
                    dps_report_status=log_data.get("dps_report_status"),
                    dps_report_name=log_data.get("dps_report_name"),
                    dps_report_notify_code=log_data.get("dps_report_notify_code"),
                    bfi_status=log_data.get("bfi_status"),
                    bfi_fight_id=log_data.get("bfi_fight_id"),
                    bfi_notify_code=log_data.get("bfi_notify_code"),
                )
            )

            if count % 100 == 0 and logs_to_save:
                is_synced = CRUDLocalLog.bulk_create_local_logs(logs_to_save)
                logs_to_save = []

        if logs_to_save:
            is_synced = CRUDLocalLog.bulk_create_local_logs(logs_to_save)

        CRUDUser.update_sync(user_id, is_synced)
        return None

    @classmethod
    def recursion_uploader_sync(
        cls, url: str, access_token: str
    ) -> tuple[bool, list[dict]]:
        if url is None or not url:
            return False, []

        response = RequestHandler.rq_get(url, access_token)
        if response is None:
            logger.error(f"recursion_uploader_sync(): response is None")
            return False, []

        is_ok, rs_data = RequestHandler.rq_status_and_data(response)
        if not is_ok:
            logger.warning(f"recursion_uploader_sync(): sync error")
            return False, []

        data = rs_data.get("data", {})

        if data.get("count") == 0:
            """nothing to sync"""
            return True, []

        all_results = data.get("results")
        next_url: str | None = data.get("next")

        if next_url is None or not next_url:
            """all pages done"""
            return True, all_results
        else:
            _next_url = next_url.replace(
                "http://127.0.0.1:8000", UploaderConstants.BFI_DOMAIN
            )
            is_sync_ok, results = cls.recursion_uploader_sync(_next_url, access_token)
            if not is_sync_ok:
                return False, []
            all_results.extend(results)

        return True, all_results
