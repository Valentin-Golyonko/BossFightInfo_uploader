from app.core.notify_constants import NotifyConstant


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

    FILE_NAME_LEN = 30
    FILE_PATH_LEN = 1000
    DPS_REPORT_NAME_LEN = 50

    MIN_LOG_SIZE = 1024

    """ LOG_UPLOAD_CODE -> """
    NOT_UPLOADED = 1
    WRONG_LOG_NAME = 2
    LOG_EXISTS = 3
    CANT_DOWNLOAD_LOG = 4
    UNKNOWN_BOSS = 5
    GOLEM_FAIL = 6
    GOLEM_RESET_BTN = 7
    EI_VERSION = 8
    LOG_AGE_LIMIT = 9
    WVW_LOG = 10
    ANONYMOUS_LOG = 11
    RAID_EI_VERSION = 12
    EMBOLDENED_MODE = 13
    BOSS_HEALTH_LIMIT = 14
    LOG_DURATION_LIMIT = 15
    DUPLICATE_LOG = 16
    PROCESSING_ERROR = 17
    LOG_UPLOADED = 18
    LOG_UPLOAD_CODE_CHOICES = (
        (NOT_UPLOADED, "Not uploaded"),
        (WRONG_LOG_NAME, NotifyConstant.WRONG_LOG_NAME),
        (LOG_EXISTS, NotifyConstant.LOG_EXISTS),
        (CANT_DOWNLOAD_LOG, NotifyConstant.CANT_DOWNLOAD_LOG),
        (UNKNOWN_BOSS, NotifyConstant.UNKNOWN_BOSS),
        (GOLEM_FAIL, NotifyConstant.GOLEM_FAIL),
        (GOLEM_RESET_BTN, NotifyConstant.GOLEM_RESET_BTN),
        (EI_VERSION, NotifyConstant.EI_VERSION),
        (LOG_AGE_LIMIT, NotifyConstant.LOG_AGE_LIMIT),
        (WVW_LOG, NotifyConstant.WVW_LOG),
        (ANONYMOUS_LOG, NotifyConstant.ANONYMOUS_LOG),
        (RAID_EI_VERSION, NotifyConstant.RAID_EI_VERSION),
        (EMBOLDENED_MODE, NotifyConstant.EMBOLDENED_MODE),
        (BOSS_HEALTH_LIMIT, NotifyConstant.BOSS_HEALTH_LIMIT),
        (LOG_DURATION_LIMIT, NotifyConstant.LOG_DURATION_LIMIT),
        (DUPLICATE_LOG, NotifyConstant.DUPLICATE_LOG),
        (PROCESSING_ERROR, NotifyConstant.PROCESSING_ERROR),
        (LOG_UPLOADED, NotifyConstant.LOG_UPLOADED),
    )
    """ <- LOG_UPLOAD_CODE """
