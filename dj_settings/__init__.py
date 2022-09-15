from __future__ import absolute_import, unicode_literals

# This will make sure the app is always imported when
# Django starts so that shared_task will use this app.
from celery_scripts.celery_app import celery_app
from dj_settings.settings import *

__all__ = ("celery_app",)
