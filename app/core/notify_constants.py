from app.core.utility_scripts.core_constants import CoreConstants


class NotifyConstant:
    """LOG_UPLOAD_CODE ->"""

    WRONG_LOG_NAME = "Wrong log name."
    LOG_EXISTS = "Log exists or in a block list."
    CANT_DOWNLOAD_LOG = "Can not download log."
    UNKNOWN_BOSS = "Unknown boss (trigger) ID."
    GOLEM_FAIL = "System accept only success golem logs."
    GOLEM_RESET_BTN = (
        f"System detected 'Mushroom King's Blessing' (skill reset) button was pressed."
        f" This is why it can't accept this log."
    )
    CURRENT_ELITE_INSIGHTS_VERSION = 2.45
    EI_VERSION = (
        f"You are using old Elite Insights version."
        f" Please update it to the latest version ({CURRENT_ELITE_INSIGHTS_VERSION}+)!"
    )
    LOG_AGE_LIMIT = (
        f"This log is too old (age more {CoreConstants.LOG_AGE_LIMIT_DAYS} days)!"
    )
    WVW_LOG = "This system can NOT process WvW logs, sorry!"
    ANONYMOUS_LOG = "This system can NOT process Anonymous logs, sorry!"
    RAID_EI_VERSION = (
        f"Raid log should be parsed with Elite Insights version"
        f" {CoreConstants.RAID_MIN_ELITE_INSIGHTS_VERSION}+ because of Emboldened mode."
    )
    EMBOLDENED_MODE = "This system can NOT process Emboldened mode logs, sorry!"
    BOSS_HEALTH_LIMIT = (
        "You can not upload log, because more than 90% Boss health left!"
    )
    LOG_DURATION_LIMIT = (
        "You can not upload log, because fight duration is less than 10 seconds!"
    )
    DUPLICATE_LOG = "Log with the same parameters exists in the system."
    PROCESSING_ERROR = "Log file processing error."
    LOG_UPLOADED = "Log uploaded."
    """ <- LOG_UPLOAD_CODE """
