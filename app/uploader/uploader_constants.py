from dj_settings.settings import DEBUG


class UploaderConstants:
    """URLs ->"""

    DPS_REPORT_URL = "https://dps.report"

    BFI_MAIN_URL = "https://gw2bossfight.info"
    BFI_DOMAIN = "http://127.0.0.1:8000" if DEBUG else BFI_MAIN_URL

    BFI_LOGIN_URL = f"{BFI_DOMAIN}/api/profile/login/"
    BFI_DUDES_URL = f"{BFI_DOMAIN}/api/profile/dudes"
    BFI_UPLOADER_SYNC_URL = f"{BFI_DOMAIN}/api/dps_report/uploader_sync/"
    BFI_UPLOADER_POST_URL = f"{BFI_DOMAIN}/api/dps_report/uploader_post/"
    """ <- URLs """
