"""
run:
    from app.uploader.logic_uploader.upload_to_dps_report import UploadToDpsReport
    UploadToDpsReport.upload_file(file_path)
"""
import logging

from app.core.logic_core.request_handler import RequestHandler
from app.core.utility_scripts.core_constants import CoreConstants

logger = logging.getLogger(__name__)


class UploadToDpsReport:
    @staticmethod
    def upload_file(file_path: str) -> tuple[dict, str]:
        response = RequestHandler.rq_log_file_upload(file_path)
        if response is None:
            return {}, CoreConstants.FILE_UPLOAD_ERROR

        is_ok, rs_data = RequestHandler.rq_status_and_data(response)
        if not is_ok:
            return {}, rs_data.get("error_msg", CoreConstants.UPLOADER_ERROR)

        return rs_data.get("data"), CoreConstants.OK
