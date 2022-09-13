from django.db import models

from app.arc_dps_log.logs_constants import LogsConstants


class LocalLog(models.Model):
    file_name = models.CharField(
        max_length=LogsConstants.FILE_NAME_LEN,
        unique=True,
        db_index=True,
    )
    file_path = models.CharField(
        max_length=LogsConstants.FILE_PATH_LEN,
    )
    file_time = models.DateTimeField(
        default=None,
        null=True,
    )

    dps_report_status = models.PositiveIntegerField(
        choices=LogsConstants.UPLOAD_STATUS_CHOICES,
        default=LogsConstants.UPLOAD_STATUS_PENDING,
        db_index=True,
    )
    dps_report_name = models.CharField(
        max_length=LogsConstants.DPS_REPORT_NAME_LEN,
        default='',
        blank=True,
    )

    bfi_status = models.PositiveIntegerField(
        choices=LogsConstants.UPLOAD_STATUS_CHOICES,
        default=LogsConstants.UPLOAD_STATUS_PENDING,
        db_index=True,
    )
    bfi_fight_id = models.PositiveBigIntegerField(
        default=None,
        null=True,
        blank=True,
    )
    bfi_notify_code = models.PositiveIntegerField(
        choices=LogsConstants.LOG_UPLOAD_CODE_CHOICES,
        default=LogsConstants.NOT_UPLOADED,
    )

    def __str__(self):
        return f"LocalLog '{self.file_name}'"

    class Meta:
        ordering = ("-file_time",)
