import logging
import os
from datetime import datetime
from functools import wraps
from time import perf_counter
from zoneinfo import ZoneInfo

logger = logging.getLogger(__name__)


def time_it(func):
    @wraps(func)
    def timed(*args, **kwargs):
        t0 = perf_counter()
        result = func(*args, **kwargs)
        logger.debug(f"time_it(): {func.__name__}() = {(perf_counter() - t0):.6f}")
        return result

    return timed


def file_created_time(file_path: str) -> datetime | None:
    try:
        return datetime.fromtimestamp(os.path.getmtime(file_path), tz=ZoneInfo("UTC"))
    except Exception as ex:
        logger.error(f"file_name_to_time(): file time Ex; {ex = }")
        return None
