from django.views.generic import ListView

from app.arc_dps_log.models import LocalLog


class LogsListView(ListView):
    template_name = "logs_list.html"
    model = LocalLog
    paginate_by = 15
    context_object_name = "logs_list"
    queryset = LocalLog.objects.defer("file_path", "file_time")
