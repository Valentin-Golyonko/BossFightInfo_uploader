"""
debug:
    from app.arc_dps_log.logic_logs.store_logs import StoreLogs
    StoreLogs.store_logs()
or:
    from app.arc_dps_log.tasks import task_store_logs
    task_store_logs.s().apply_async()
"""
import logging

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
            if is_file_ok:
                dps_report_status = LogsConstants.UPLOAD_STATUS_PENDING
                bfi_status = LogsConstants.UPLOAD_STATUS_PENDING
            else:
                dps_report_status = LogsConstants.UPLOAD_STATUS_BROKEN
                bfi_status = LogsConstants.UPLOAD_STATUS_BROKEN

            logs_to_save.append(
                LocalLog(
                    file_name=file_name,
                    file_path=file_path,
                    file_time=modify_time,
                    dps_report_status=dps_report_status,
                    bfi_status=bfi_status,
                )
            )

            if count % 100 == 0 and logs_to_save:
                CRUDLocalLog.bulk_create_local_logs(logs_to_save)
                logs_to_save = []

        if logs_to_save:
            CRUDLocalLog.bulk_create_local_logs(logs_to_save)

        return None
