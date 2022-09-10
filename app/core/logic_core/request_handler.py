import logging
from http import HTTPStatus

import requests
from requests import Response

from app.core.utility_scripts.core_constants import CoreConstants

logger = logging.getLogger(__name__)


class RequestHandler:

    @staticmethod
    def rq_post(url: str, data: dict) -> Response | None:
        try:
            return requests.post(
                url=url,
                json=data,
            )
        except Exception as ex:
            logger.error(f"rq_post(): requests Ex; {url = }; {ex = }")
            return None

    @staticmethod
    def rq_json(response: Response) -> dict | None:
        try:
            return response.json()
        except Exception as ex:
            logger.error(f"rq_json(): response.json Ex;"
                         f" {response.url = }, {response.status_code = };"
                         f" {ex = }")
            return None

    @staticmethod
    def rq_error_msg(rs_data: dict) -> str:
        if rs_data is None:
            return CoreConstants.CONNECTION_ERROR
        return rs_data.get("detail", CoreConstants.CONNECTION_ERROR)

    @classmethod
    def rq_status_and_data(cls, response: Response) -> tuple[bool, dict]:
        rs_data = cls.rq_json(response)
        match response.status_code:
            case HTTPStatus.OK:
                return True, {"data": rs_data, "error_msg": None}
            case _:
                return False, {"data": None, "error_msg": cls.rq_error_msg(rs_data)}
