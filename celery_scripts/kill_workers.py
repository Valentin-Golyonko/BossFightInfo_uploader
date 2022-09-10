"""
run:
    python manage.py runscript celery_scripts.kill_workers
"""
import logging

from celery_scripts.restart_workers import RestartWorkers
from app.core import CoreConstants

logger = logging.getLogger(__name__)


def run() -> None:
    RestartWorkers.kill_celery_worker(
        worker_name=CoreConstants.DEFAULT_WORKER_NAME,
    )
    return None
