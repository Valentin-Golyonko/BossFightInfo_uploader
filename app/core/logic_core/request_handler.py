import logging
from http import HTTPStatus
from typing import IO

import requests
from requests import Response

from app.core.utility_scripts.core_constants import CoreConstants
from app.uploader.uploader_constants import UploaderConstants

logger = logging.getLogger(__name__)


class RequestHandler:
    @staticmethod
    def rq_post(url: str, json_data: dict, access_token: str = None) -> Response | None:
        try:
            if access_token is None:
                return requests.post(
                    url=url,
                    json=json_data,
                )
            else:
                return requests.post(
                    url=url,
                    headers={"Authorization": f"Bearer {access_token}"},
                    json=json_data,
                )
        except Exception as ex:
            logger.error(f"rq_post(): requests Ex; {url = }; {ex = }")
            return None

    @staticmethod
    def rq_json(response: Response) -> dict:
        try:
            return response.json()
        except Exception as ex:
            logger.error(
                f"rq_json(): response.json Ex;"
                f" {response.url = }, {response.status_code = };"
                f" {ex = }"
            )
            return {}

    @staticmethod
    def rq_error_msg(rs_data: dict) -> str:
        if rs_data is None:
            return CoreConstants.UPLOADER_ERROR
        return rs_data.get("detail", CoreConstants.UPLOADER_ERROR)

    @classmethod
    def rq_status_and_data(cls, response: Response) -> tuple[bool, dict]:
        if response is None:
            return False, {"data": {}, "error_msg": CoreConstants.UPLOADER_ERROR}

        rs_data = cls.rq_json(response)
        match response.status_code:
            case HTTPStatus.OK:
                return True, {"data": rs_data, "error_msg": CoreConstants.OK}
            case _:
                return False, {"data": rs_data, "error_msg": cls.rq_error_msg(rs_data)}

    @staticmethod
    def rq_log_file_upload(file_io: IO) -> Response | None:
        try:
            return requests.post(
                url=f"{UploaderConstants.DPS_REPORT_URL}/uploadContent",
                data={
                    "json": 1,
                },
                files={
                    "file": file_io,
                },
            )
        except Exception as ex:
            logger.error(f"rq_log_file_upload(): Ex; {ex = }")
            return None

    @staticmethod
    def rq_get(url: str, access_token: str = None) -> Response | None:
        try:
            if access_token is None:
                return requests.get(url=url)
            else:
                return requests.get(
                    url=url,
                    headers={"Authorization": f"Bearer {access_token}"},
                )
        except Exception as ex:
            logger.error(f"rq_get(): requests Ex; {url = }; {ex = }")
            return None
