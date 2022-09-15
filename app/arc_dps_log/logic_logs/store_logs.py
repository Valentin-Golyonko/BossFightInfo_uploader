"""
debug:
    from app.arc_dps_log.logic_logs.store_logs import StoreLogs
    StoreLogs.store_logs()
or:
    from app.arc_dps_log.tasks import task_store_logs
    task_store_logs.s().apply_async()
"""
import logging
from datetime import datetime

from django.utils.timezone import now

from app.arc_dps_log.logic_logs.crud_local_log import CRUDLocalLog
from app.arc_dps_log.logic_logs.find_local_logs import FindLocalLogs
from app.arc_dps_log.logs_constants import LogsConstants
from app.arc_dps_log.models import LocalLog
from app.core.utility_scripts.util_scripts import time_it, CheckFile

logger = logging.getLogger(__name__)


class StoreLogs:
    @classmethod
    @time_it
    def store_logs(cls) -> None:
        files_paths, logs_names = FindLocalLogs.find_logs()
        db_logs_names = CRUDLocalLog.list_logs_names()
        not_stored_logs = set(logs_names).difference(db_logs_names)

        logs_to_save = []
        count = 0
        for file_path, file_name in zip(files_paths, logs_names):
            if file_name not in not_stored_logs:
                """skip already stored logs"""
                continue

            count += 1
            is_file_ok, modify_time = CheckFile.check_log_stats(file_path)
            limitations_data = cls.check_limitations(is_file_ok, modify_time, file_path)

            logs_to_save.append(
                LocalLog(
                    file_name=file_name,
                    file_path=file_path,
                    file_time=modify_time,
                    dps_report_status=limitations_data.get("dps_report_status"),
                    dps_report_notify_code=limitations_data.get(
                        "dps_report_notify_code"
                    ),
                    bfi_status=limitations_data.get("bfi_status"),
                    bfi_notify_code=limitations_data.get("bfi_notify_code"),
                )
            )

            if count % 100 == 0 and logs_to_save:
                CRUDLocalLog.bulk_create_local_logs(logs_to_save)
                logs_to_save = []

        if logs_to_save:
            CRUDLocalLog.bulk_create_local_logs(logs_to_save)

        return None

    @staticmethod
    def check_limitations(
        is_file_ok: bool,
        modify_time: datetime,
        file_path: str,
    ) -> dict:

        if not is_file_ok or modify_time is None:
            dps_report_status = LogsConstants.UPLOAD_STATUS_BROKEN
            dps_report_notify_code = LogsConstants.CANT_UPLOAD
            bfi_status = LogsConstants.UPLOAD_STATUS_BROKEN
            bfi_notify_code = LogsConstants.CANT_UPLOAD

        elif (now() - modify_time).days > LogsConstants.LOG_AGE_LIMIT_DAYS:
            dps_report_status = LogsConstants.UPLOAD_STATUS_LIMITS
            dps_report_notify_code = LogsConstants.LOG_AGE_LIMIT
            bfi_status = LogsConstants.UPLOAD_STATUS_LIMITS
            bfi_notify_code = LogsConstants.LOG_AGE_LIMIT

        elif len(file_path) > LogsConstants.FILE_PATH_LEN:
            dps_report_status = LogsConstants.UPLOAD_STATUS_LIMITS
            dps_report_notify_code = LogsConstants.FILE_PATH_TOO_LONG
            bfi_status = LogsConstants.UPLOAD_STATUS_LIMITS
            bfi_notify_code = LogsConstants.FILE_PATH_TOO_LONG

        else:
            """all good"""
            dps_report_status = LogsConstants.UPLOAD_STATUS_PENDING
            dps_report_notify_code = LogsConstants.NOT_UPLOADED
            bfi_status = LogsConstants.UPLOAD_STATUS_PENDING
            bfi_notify_code = LogsConstants.NOT_UPLOADED

        return {
            "dps_report_status": dps_report_status,
            "dps_report_notify_code": dps_report_notify_code,
            "bfi_status": bfi_status,
            "bfi_notify_code": bfi_notify_code,
        }
