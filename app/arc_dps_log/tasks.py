"""
run:
    from app.arc_dps_log.tasks import task_store_logs
    task_store_logs.apply_async()
"""
import logging

from app.arc_dps_log.logic_logs.store_logs import StoreLogs
from app.core.utility_scripts.core_constants import CoreConstants
from celery_scripts.celery_app import celery_app

logger = logging.getLogger(__name__)


@celery_app.task(
    name=f"{CoreConstants.DEFAULT_TASK_PREFIX}_task.store_logs",
    queue=CoreConstants.DEFAULT_QUEUE,
    ignore_result=True,
)
def task_store_logs() -> None:
    try:
        StoreLogs.store_logs()
    except Exception as ex:
        logger.exception(f"task_store_logs(): Ex; {ex = }")
    else:
        logger.info(f"task_store_logs(): Done")
    return None
