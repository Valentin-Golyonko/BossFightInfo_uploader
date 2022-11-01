"""
debug:
    from app.uploader.logic_uploader.upload_to_bfi import UploadToBFi
    UploadToBFi.upload_to_bfi(log_data, log_id, auth_str)
"""
import logging

from app.arc_dps_log.logic_logs.crud_local_log import CRUDLocalLog
from app.core.logic_core.request_handler import RequestHandler
from app.core.utility_scripts.util_scripts import ConvertDateTime
from app.uploader.uploader_constants import UploaderConstants

logger = logging.getLogger(__name__)


class UploadToBFi:
    @staticmethod
    def upload_to_bfi(log_data: dict, log_id: int, access_token: str) -> None:
        modify_time_iso = ConvertDateTime.dt_to_iso(log_data.get("file_time"))
        if modify_time_iso is None:
            CRUDLocalLog.delete_local_log(log_id)
            return None

        log_data["file_time"] = modify_time_iso
        response = RequestHandler.rq_post(
            url=UploaderConstants.BFI_UPLOADER_POST_URL,
            json_data=log_data,
            access_token=access_token,
        )

        if response is None:
            logger.error(f"upload_to_bfi(): response is None; {log_id = }")
            return None

        is_ok, rs_data = RequestHandler.rq_status_and_data(response)
        data: dict = rs_data.get("data")
        if not is_ok:
            if data.get("bfi_notify_code") is None:
                logger.error(f"upload_to_bfi(): bfi_notify_code is None; {data = }")
                return None

        CRUDLocalLog.update_log_after_upload(
            log_id=log_id,
            from_dps_report=False,
            from_bfi=True,
            new_data={
                "bfi_status": data.get("bfi_status"),
                "bfi_fight_id": data.get("bfi_fight_id"),
                "bfi_notify_code": data.get("bfi_notify_code"),
            },
        )
        return None
