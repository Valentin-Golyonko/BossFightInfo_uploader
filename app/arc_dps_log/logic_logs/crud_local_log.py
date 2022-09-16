import logging

from django.db.utils import IntegrityError

from app.arc_dps_log.logs_constants import LogsConstants
from app.arc_dps_log.models import LocalLog

logger = logging.getLogger(__name__)


class CRUDLocalLog:
    @staticmethod
    def list_logs_names() -> list[str]:
        try:
            return LocalLog.objects.values_list(
                "file_name",
                flat=True,
            )
        except Exception as ex:
            logger.error(f"list_logs_names(): values_list Ex; {ex = }")
            return []

    @staticmethod
    def bulk_create_local_logs(logs_to_save: list[LocalLog]) -> bool:
        try:
            LocalLog.objects.bulk_create(
                logs_to_save,
                update_conflicts=True,
                update_fields=[
                    "file_path",
                    "file_time",
                    "dps_report_status",
                    "dps_report_name",
                    "bfi_status",
                    "bfi_fight_id",
                    "bfi_notify_code",
                ],
                unique_fields=["file_name"],
            )
        except IntegrityError:
            logger.error(f"bulk_create_local_logs(): IntegrityError Ex")
            return False
        except Exception as ex:
            logger.error(f"bulk_create_local_logs(): bulk_create Ex; {ex = }")
            return False
        else:
            return True

    @staticmethod
    def list_logs_to_upload(to_dps_report: bool, to_bfi: bool) -> list[dict]:
        try:
            if to_dps_report:
                return LocalLog.objects.filter(
                    dps_report_status=LogsConstants.UPLOAD_STATUS_PENDING
                ).values("id", "file_path")
            elif to_bfi:
                return (
                    LocalLog.objects.filter(
                        dps_report_status=LogsConstants.UPLOAD_STATUS_OK,
                        bfi_status=LogsConstants.UPLOAD_STATUS_PENDING,
                    )
                    .exclude(
                        dps_report_name="",
                    )
                    .values()
                )
            else:
                return []
        except Exception as ex:
            logger.error(f"list_logs_to_upload(): LocalLog.filter Ex; {ex = }")
            return []

    @staticmethod
    def update_log_after_upload(
        log_id: int, from_dps_report: bool, from_bfi: bool, new_data: dict
    ) -> None:
        try:
            if from_dps_report:
                LocalLog.objects.filter(id=log_id).update(
                    dps_report_status=new_data.get("dps_report_status"),
                    dps_report_name=new_data.get("dps_report_name"),
                    dps_report_notify_code=new_data.get("dps_report_notify_code"),
                )
            elif from_bfi:
                LocalLog.objects.filter(id=log_id).update(
                    bfi_status=new_data.get("bfi_status"),
                    bfi_fight_id=new_data.get("bfi_fight_id"),
                    bfi_notify_code=new_data.get("bfi_notify_code"),
                )
        except Exception as ex:
            logger.error(
                f"update_log_after_upload(): LocalLog.update Ex; {log_id = } {ex = }"
            )
        return None

    @staticmethod
    def delete_local_log(log_id: int) -> None:
        try:
            LocalLog.objects.filter(id=log_id).delete()
        except Exception as ex:
            logger.error(f"delete_local_log(): LocalLog.delete Ex; {log_id = } {ex = }")
        return None
