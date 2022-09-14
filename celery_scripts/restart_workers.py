"""
run:
    python manage.py runscript celery_scripts.restart_workers
"""
import logging
import os
from time import sleep

from app.core.utility_scripts.core_constants import CoreConstants
from app.core.utility_scripts.util_scripts import time_it
from dj_settings.settings import DEBUG

logger = logging.getLogger(__name__)


def run() -> None:
    RestartWorkers.restart_workers()
    return None


class RestartWorkers:
    @classmethod
    @time_it
    def restart_workers(cls) -> None:
        if DEBUG:
            log_lvl = "info"
        else:
            log_lvl = "warning"

        cls.kill_celery_worker(
            worker_name=CoreConstants.DEFAULT_WORKER_NAME,
        )
        cls.start_celery_worker(
            worker_name=CoreConstants.DEFAULT_WORKER_NAME,
            queue_name=CoreConstants.DEFAULT_QUEUE,
            concurrency_number=CoreConstants.DEFAULT_CONCURRENCY,
            log_lvl=log_lvl,
            with_beat=True,
        )
        return None

    @staticmethod
    def kill_celery_worker(worker_name: str) -> None:
        try:
            """find worker pid file"""
            stream = os.popen(f"ls ./logs/{worker_name}_worker.pid")
            if worker_pid_file := [i for i in str(stream.read()).split("\n") if i]:
                with open(worker_pid_file[0], "r") as pid_file:
                    pid_id = str(pid_file.read()).replace("\n", "")
                    """ kill worker process """
                    os.system(f"kill -HUP {pid_id}")
                    pid_file.close()
        except Exception as ex:
            msg = f"kill_celery_worker(): kill -HUP Ex; {worker_name = }; {ex = }"
            logger.error(msg)
        else:
            logger.info(
                f"kill_celery_worker(): celery worker stopped;" f" {worker_name = }"
            )
            """ wait server to stop precess """
            sleep(2)

            if worker_pid_file:
                try:
                    """remove worker pid file if not self-deleted"""
                    os.system(f"rm {worker_pid_file[0]}")
                except Exception as ex:
                    msg = (
                        f"kill_celery_worker(): rm worker_pid_file Ex;"
                        f" {worker_name = }; {ex = }"
                    )
                    logger.error(msg)

        return None

    @staticmethod
    def start_celery_worker(
        worker_name: str,
        queue_name: str,
        concurrency_number: int,
        log_lvl: str,
        with_beat: bool,
    ) -> None:
        try:
            os.system(
                f"celery multi start worker"
                f" --app=dj_settings"
                f" --loglevel={log_lvl}"
                f" --concurrency={concurrency_number}"
                f" {'--beat' if with_beat else ''}"
                f" --queues={queue_name}"
                f" --hostname=bfi_{queue_name}@%n"
                f" --pidfile=./logs/{worker_name}_%n.pid"
                f" --logfile=./logs/{worker_name}_%n.log"
            )
        except Exception as ex:
            msg = (
                f"start_celery_worker(): celery multi start worker Ex;"
                f" {worker_name = }, {queue_name = }; {ex = }"
            )
            logger.error(msg)
        else:
            logger.info(f"start_celery_worker(): celery worker started")

        return None
