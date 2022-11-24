import logging

from django.shortcuts import redirect
from django.views.generic import ListView

from app.arc_dps_log.logic_logs.store_logs import StoreLogs
from app.arc_dps_log.logic_logs.uploader_sync import UploaderSync
from app.arc_dps_log.models import LocalLog

logger = logging.getLogger(__name__)


class LogsListView(ListView):
    template_name = "logs_list.html"
    model = LocalLog
    paginate_by = 15
    context_object_name = "logs_list"
    queryset = LocalLog.objects.defer("file_path", "file_time")


def sync_uploader_view(request, *args, **kwargs):
    try:
        UploaderSync.get_data_from_bfi()
    except Exception as ex:
        logger.exception(f"sync_uploader_view(): get_data_from_bfi Ex; {ex = }")

    return redirect(to="arc_dps_log:logs_list")


def find_local_logs_view(request, *args, **kwargs):
    try:
        StoreLogs.store_logs()
    except Exception as ex:
        logger.exception(f"find_local_logs_view(): store_logs Ex; {ex = }")

    return redirect(to="arc_dps_log:logs_list")
