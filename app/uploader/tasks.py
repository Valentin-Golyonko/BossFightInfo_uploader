"""
run:
    from app.uploader.tasks import task_upload_logs
    task_upload_logs.s().apply_async()
"""
import logging

from app.core.utility_scripts.core_constants import CoreConstants
from app.uploader.logic_uploader.upload_flow import UploadFlow
from celery_scripts.celery_app import celery_app

logger = logging.getLogger(__name__)


@celery_app.task(
    name=f"{CoreConstants.DEFAULT_TASK_PREFIX}_task.upload_logs",
    queue=CoreConstants.DEFAULT_QUEUE,
    ignore_result=True,
)
def task_upload_logs() -> None:
    try:
        UploadFlow.upload_local_logs()
    except Exception as ex:
        logger.exception(f"task_upload_logs(): Ex; {ex = }")
    else:
        logger.info(f"task_upload_logs(): Done")
    return None
