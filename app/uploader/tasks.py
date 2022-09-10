import logging

from app.core.utility_scripts.core_constants import CoreConstants
from celery_scripts.celery_app import celery_app


logger = logging.getLogger(__name__)


@celery_app.task(
    name=f"{CoreConstants.DEFAULT_TASK_PREFIX}_task.upload_log",
    queue=CoreConstants.DEFAULT_QUEUE,
    ignore_result=True,
)
def task_upload_log() -> None:
    try:
        # TODO
        pass
    except Exception as ex:
        logger.exception(f"task_upload_log(): Ex; {ex = }")
    else:
        logger.info(f"task_upload_log(): Done")
    return None
