from django.contrib import admin

from app.arc_dps_log.models import LocalLog


@admin.register(LocalLog)
class LocalLogAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "file_name",
        "dps_report_name",
        "dps_report_status",
        "bfi_status",
    )
    search_fields = (
        "file_name",
        "dps_report_name",
    )

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False
