class CoreConstants:
    """ Celery -> """
    DEFAULT_QUEUE = "celery"
    DEFAULT_WORKER_NAME = "main"
    DEFAULT_CONCURRENCY = 1
    DEFAULT_TASK_PREFIX = "main"
    """ <- Celery """

    """ Symbols -> """
    MDASH_SYMBOL = "—"
    NA_STR = "n/a"
    SOON_TM = "Soon™"
    """ <- Symbols """

    """ Datetime -> """
    DATE_TIME_FORMAT = "%a, %d %b %Y %H:%M:%S"
    DATE_TIME_FORMAT_TZ = "%a, %d %b %Y %H:%M:%S %z"
    DATE_FORMAT = "%a, %d %b %Y"
    DAY_MONTH_FORMAT = "%d/%m"
    Y_M_D_FORMAT = "%Y-%m-%d"
    Y_M_D_H_M_FORMAT = "%Y-%m-%d %H:%M"
    """ <- Datetime """

    """ URLs -> """
    DPS_REPORT_URL = "https://dps.report"
    BFI_MAIN_URL = "https://gw2bossfight.info"
    BFI_LOGIN_URL = "https://gw2bossfight.info/api/profile/login/"
    BFI_USER_DATA = "https://gw2bossfight.info/api/profile/dudes"
    BFI_MULTI_LOG_UPLOAD_URL = "https://gw2bossfight.info/api/dps_report/multi_log_upload/"
    """ <- URLs """

    """ Errors -> """
    OK = "OK"
    UPLOADER_ERROR = "Internal uploader error."
    UNKNOWN_ERROR = "Unknown error."
    CONNECTION_ERROR = "Error connecting to gw2bossfight.info"
    FILE_UPLOAD_ERROR = "File upload error."
    CREATE_USER_ERROR = "Can't create user for the uploader."
    UPLOADER_LOGIN_FAIL = "Failed to login to the uploader."
    """ <- Errors """

    LOG_FILE_FORMATS = (
        "evtc",
        "evtc.zip",
        "zevtc",
    )

    GW2_ACCOUNT_LEN = 50
    GW2_API_KEY_LEN = 200
