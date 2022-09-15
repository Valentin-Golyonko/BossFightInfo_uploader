"""
debug:
    from app.arc_dps_log.logic_logs.uploader_sync import UploaderSync
    UploaderSync.get_data_from_bfi()
"""
import logging

from app.arc_dps_log.logic_logs.crud_local_log import CRUDLocalLog
from app.arc_dps_log.models import LocalLog
from app.core.logic_core.request_handler import RequestHandler
from app.core.utility_scripts.util_scripts import time_it
from app.uploader.uploader_constants import UploaderConstants
from app.user.logic_user.crud_user import CRUDUser

logger = logging.getLogger(__name__)


class UploaderSync:
    @classmethod
    @time_it
    def get_data_from_bfi(cls) -> None:
        user_obj = CRUDUser.get_uploader_user()
        if user_obj is None:
            logger.error(f"get_data_from_bfi(): no user for sync")
            return None

        results = cls.recursion_uploader_sync(
            url=UploaderConstants.BFI_UPLOADER_SYNC_URL,
            auth_str=user_obj.auth_str,
        )
        if not results:
            return None

        db_logs_names = CRUDLocalLog.list_logs_names()

        logs_to_save = []
        count = 0
        for log_data in results:
            file_name = log_data.get("file_name")
            if file_name in db_logs_names:
                """skip already stored logs"""
                continue

            count += 1

            logs_to_save.append(
                LocalLog(
                    file_name=file_name,
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
                CRUDLocalLog.bulk_create_local_logs(logs_to_save)
                logs_to_save = []

        if logs_to_save:
            CRUDLocalLog.bulk_create_local_logs(logs_to_save)

        return None

    @classmethod
    def recursion_uploader_sync(cls, url: str, auth_str: str) -> list[dict]:
        if url is None or not url:
            return []

        response = RequestHandler.rq_get(url, auth_str)
        if response is None:
            logger.error(f"recursion_uploader_sync(): response is None")
            return []

        is_ok, rs_data = RequestHandler.rq_status_and_data(response)
        if not is_ok:
            logger.warning(f"recursion_uploader_sync(): sync error")
            return []

        data = rs_data.get("data", {})

        if data.get("count") == 0:
            logger.debug(f"recursion_uploader_sync(): nothing to sync")
            return []

        all_results = data.get("results")
        next_url: str | None = data.get("next")

        if next_url is None or not next_url:
            return all_results
        else:
            all_results.extend(cls.recursion_uploader_sync(next_url, auth_str))

        return all_results
