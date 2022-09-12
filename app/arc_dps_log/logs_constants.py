class LogsConstants:
    UPLOAD_STATUS_OK = 1
    UPLOAD_STATUS_PENDING = 2
    UPLOAD_STATUS_ERROR = 3
    UPLOAD_STATUS_BROKEN = 4
    UPLOAD_STATUS_CHOICES = (
        (UPLOAD_STATUS_OK, "ok"),
        (UPLOAD_STATUS_PENDING, "pending"),
        (UPLOAD_STATUS_ERROR, "error"),
        (UPLOAD_STATUS_BROKEN, "broken file"),
    )
