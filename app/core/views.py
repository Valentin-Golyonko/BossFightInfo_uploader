from django.shortcuts import render
from django.views.generic import TemplateView


class LogsListView(TemplateView):
    template_name = "logs_list.html"

    def get(self, request, *args, **kwargs):
        logs_list = [
            {
                "id": i,
                "file_name": f"test file {i}",
                "log_link": f"log link {i}",
            } for i in range(10)
        ]
        return render(request, self.template_name, {'logs_list': logs_list})

