import logging

from django.db.utils import IntegrityError

from app.arc_dps_log.models import LocalLog

logger = logging.getLogger(__name__)


class CRUDLocalLog:
    @staticmethod
    def log_by_file_name(file_name: str) -> bool:
        try:
            return LocalLog.objects.filter(file_name=file_name).exists()
        except Exception as ex:
            logger.error(f"log_by_file_name(): exists Ex; {file_name = }; {ex = }")
            return False

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
    def bulk_create_local_logs(logs_to_save: list[LocalLog]) -> None:
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
        except Exception as ex:
            logger.error(f"bulk_create_local_logs(): bulk_create Ex; {ex = }")
        return None
