import logging
import os
from datetime import datetime

from django.db.utils import IntegrityError

from app.arc_dps_log.models import LocalLog

logger = logging.getLogger(__name__)


class CRUDLocalLog:

    @classmethod
    def create_local_log_obj(cls, log_data: dict) -> LocalLog | None:
        file_name = log_data.get("file_name")
        file_path = log_data.get("file_path")
        try:
            return LocalLog.objects.create(
                file_name=file_name,
                file_path=file_path,
                file_time=cls.file_created_time(file_path),
                dps_report_status=log_data.get("dps_report_status"),
                dps_report_name=log_data.get("dps_report_name"),
                bfi_status=log_data.get("bfi_status"),
                bfi_fight_id=log_data.get("bfi_fight_id"),
            )
        except IntegrityError:
            logger.warning(f"create_local_log_obj(): IntegrityError; {file_name = }")
        except Exception as ex:
            logger.error(f"create_local_log_obj(): create Ex; {file_name = }; {ex = }")
        return None

    @staticmethod
    def log_by_file_name(file_name: str) -> bool:
        try:
            return LocalLog.objects.filter(file_name=file_name).exists()
        except Exception as ex:
            logger.error(f"log_by_file_name(): exists Ex; {file_name = }; {ex = }")
            return False

    @staticmethod
    def file_created_time(file_path: str) -> datetime | None:
        try:
            return datetime.fromtimestamp(os.path.getmtime(file_path))
        except Exception as ex:
            logger.error(f"file_name_to_time(): file time Ex; {ex = }")
            return None
