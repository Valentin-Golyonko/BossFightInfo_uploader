import logging
import os
from datetime import datetime
from functools import wraps
from pathlib import Path
from time import perf_counter
from typing import IO
from zoneinfo import ZoneInfo

from app.arc_dps_log.logs_constants import LogsConstants

logger = logging.getLogger(__name__)


def time_it(func):
    @wraps(func)
    def timed(*args, **kwargs):
        t0 = perf_counter()
        result = func(*args, **kwargs)
        logger.debug(f"time_it(): {func.__name__}() = {(perf_counter() - t0):.6f}")
        return result

    return timed


class CheckFile:
    @staticmethod
    def check_log_stats(log_path) -> tuple[bool, datetime | None]:
        try:
            file_stats = os.stat(log_path)
        except Exception as ex:
            logger.error(f"check_log_stats(): Ex; {ex = }")
            return False, None

        modify_time = datetime.fromtimestamp(file_stats.st_mtime, tz=ZoneInfo("UTC"))

        if file_stats.st_size < LogsConstants.MIN_LOG_SIZE:
            return False, modify_time
        return True, modify_time

    @staticmethod
    def open_file(file_path: str) -> IO | None:
        try:
            if not Path(file_path).exists():
                return None
        except Exception as ex:
            logger.error(f"open_file(): Path Ex; {file_path = }; {ex = }")
            return None

        try:
            return open(file_path, "rb")
        except Exception as ex:
            logger.error(f"open_file(): open Ex; {file_path = }; {ex = }")
            return None


class ConvertDateTime:
    @staticmethod
    def dt_to_iso(dt: datetime) -> str | None:
        try:
            return dt.isoformat()
        except Exception as ex:
            logger.error(f"dt_to_iso(): Ex; {dt = }; {ex = }")
            return None
