class CoreConstants:
    DEFAULT_QUEUE = "celery"
    DEFAULT_WORKER_NAME = "main"
    DEFAULT_CONCURRENCY = 1
    DEFAULT_TASK_PREFIX = "main"

    DPS_REPORT_URL = "https://dps.report"

    MDASH_SYMBOL = "—"
    NA_STR = "n/a"
    SOON_TM = "Soon™"

    DATE_TIME_FORMAT = "%a, %d %b %Y %H:%M:%S"
    DATE_TIME_FORMAT_TZ = "%a, %d %b %Y %H:%M:%S %z"
    DATE_FORMAT = "%a, %d %b %Y"
    DAY_MONTH_FORMAT = "%d/%m"
    Y_M_D_FORMAT = "%Y-%m-%d"
    Y_M_D_H_M_FORMAT = "%Y-%m-%d %H:%M"

    BFI_MAIN_URL = "https://gw2bossfight.info"
    BFI_LOGIN_URL = "https://gw2bossfight.info/api/profile/login/"
    BFI_MULTI_LOG_UPLOAD_URL = "https://gw2bossfight.info/api/dps_report/multi_log_upload/"

    """ Errors -> """
    OK = "OK"
    UPLOADER_ERROR = "Internal uploder error."
    UNKNOWN_ERROR = "Unknown error."
    CONNECTION_ERROR = "Error connection to gw2bossfight.info"
    FILE_UPLOAD_ERROR = "File upload error."
    """ <- Errors """
