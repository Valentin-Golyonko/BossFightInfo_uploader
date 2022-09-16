"""
debug:
    from app.uploader.logic_uploader.upload_flow import UploadFlow
    UploadFlow.upload_local_logs()
"""
import logging

from app.arc_dps_log.logic_logs.crud_local_log import CRUDLocalLog
from app.arc_dps_log.logs_constants import LogsConstants
from app.core.utility_scripts.util_scripts import time_it
from app.uploader.logic_uploader.upload_to_bfi import UploadToBFi
from app.uploader.logic_uploader.upload_to_dps_report import UploadToDpsReport
from app.user.logic_user.check_user import CheckUser

logger = logging.getLogger(__name__)


class UploadFlow:
    @staticmethod
    @time_it
    def upload_local_logs() -> None:
        is_user_ok, auth_str, user_id = CheckUser.check_user(upload=True)
        if not is_user_ok:
            return None

        logs_for_dps_report = CRUDLocalLog.list_logs_to_upload(
            to_dps_report=True,
            to_bfi=False,
        )
        for log_data_1 in logs_for_dps_report[: LogsConstants.CURRENT_UPLOAD_LIMIT]:
            UploadToDpsReport.upload_to_dps_report(
                file_path=log_data_1.get("file_path"),
                log_id=log_data_1.get("id"),
            )

        logs_for_bfi = CRUDLocalLog.list_logs_to_upload(
            to_dps_report=False,
            to_bfi=True,
        )
        for log_data_2 in logs_for_bfi[: LogsConstants.CURRENT_UPLOAD_LIMIT]:
            UploadToBFi.upload_to_bfi(
                log_data=log_data_2,
                log_id=log_data_2.get("id"),
                auth_str=auth_str,
            )

        return None
