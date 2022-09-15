"""
debug:
    from app.uploader.logic_uploader.upload_to_dps_report import UploadToDpsReport
    UploadToDpsReport.upload_to_dps_report(file_path, log_id)
"""
import logging

from app.arc_dps_log.logic_logs.crud_local_log import CRUDLocalLog
from app.arc_dps_log.logs_constants import LogsConstants
from app.core.logic_core.request_handler import RequestHandler
from app.core.utility_scripts.util_scripts import CheckFile

logger = logging.getLogger(__name__)


class UploadToDpsReport:
    @classmethod
    def upload_to_dps_report(cls, file_path: str, log_id: int) -> None:
        file_io = CheckFile.open_file(file_path)
        if file_io is None:
            CRUDLocalLog.delete_local_log(log_id)
            return None

        response = RequestHandler.rq_log_file_upload(file_io)
        if response is None:
            logger.error(f"upload_to_dps_report(): response is None; {log_id = }")
            return None

        is_ok, rs_data = RequestHandler.rq_status_and_data(response)
        data: dict = rs_data.get("data")
        if not is_ok:
            # TODO: check status code; server may be down -> do not change log status
            error = data.get("error")
            logger.error(
                f"upload_to_dps_report(): dps.report error;"
                f" {log_id = }, {response.status_code = }, {error = }"
            )
            dps_report_status = LogsConstants.UPLOAD_STATUS_ERROR
            dps_report_name = ""
            dps_report_notify_code = LogsConstants.CANT_UPLOAD
        else:
            dps_report_name = cls.permalink_to_report_name(data.get("permalink"))
            if dps_report_name is None:
                dps_report_status = LogsConstants.UPLOAD_STATUS_ERROR
                dps_report_notify_code = LogsConstants.CANT_UPLOAD
            else:
                dps_report_status = LogsConstants.UPLOAD_STATUS_OK
                dps_report_notify_code = LogsConstants.LOG_UPLOADED

        CRUDLocalLog.update_log_after_upload(
            log_id=log_id,
            from_dps_report=True,
            from_bfi=False,
            new_data={
                "dps_report_status": dps_report_status,
                "dps_report_name": dps_report_name,
                "dps_report_notify_code": dps_report_notify_code,
            },
        )
        return None

    @staticmethod
    def permalink_to_report_name(permalink: str) -> str | None:
        if permalink is None or not permalink:
            return None
        try:
            return permalink.split("/")[-1]
        except Exception as ex:
            logger.error(f"permalink_to_report_name(): Ex; {permalink = }; {ex = }")
            return None
