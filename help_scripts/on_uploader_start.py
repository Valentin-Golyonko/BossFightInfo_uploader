"""
run:
    python manage.py runscript help_scripts.on_uploader_start
"""
from app.arc_dps_log.tasks import task_uploader_sync


def run() -> None:
    task_uploader_sync.apply_async()
    return None
