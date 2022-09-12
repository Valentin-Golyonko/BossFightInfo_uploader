from django.shortcuts import render
from django.views.generic import TemplateView

from app.arc_dps_log.models import LocalLog


class LogsListView(TemplateView):
    template_name = "logs_list.html"

    def get(self, request, *args, **kwargs):
        logs_list = []
        for log_obj in LocalLog.objects.defer("file_time").all()[:20]:
            logs_list.append({
                "id": log_obj.id,
                "file_name": log_obj.file_name,
                "file_path": log_obj.file_path,
                "dps_report_status": log_obj.dps_report_status,
                "dps_report_status_name": log_obj.get_dps_report_status_display(),
                "dps_report_name": log_obj.dps_report_name,
                "bfi_status": log_obj.bfi_status,
                "bfi_status_name": log_obj.get_bfi_status_display(),
                "bfi_fight_id": log_obj.bfi_fight_id,
            })
        return render(request, self.template_name, {'logs_list': logs_list})
