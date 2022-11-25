import logging

from django.shortcuts import redirect

from app.uploader.logic_uploader.upload_flow import UploadFlow

logger = logging.getLogger(__name__)


def upload_log_view(request, *args, **kwargs):
    try:
        UploadFlow.upload_one_log(kwargs.get("id", 0))
    except Exception as ex:
        logger.exception(f"upload_logs_view(): store_logs Ex; {ex = }")

    return redirect(to=request.META.get("HTTP_REFERER", "arc_dps_log:logs_list"))
