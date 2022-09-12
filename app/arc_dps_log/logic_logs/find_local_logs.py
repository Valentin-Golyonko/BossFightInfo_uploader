"""
run:
    from app.arc_dps_log.logic_logs.find_local_logs import FindLocalLogs
    FindLocalLogs.find_logs()
"""
import logging
import os
from pathlib import Path

from dj_settings.settings import BASE_DIR

logger = logging.getLogger(__name__)


class FindLocalLogs:

    @classmethod
    def find_logs(cls) -> list[str]:
        # cd /d E:\PycharmProjects\BossFightInfo_uploader\user_arcdps_logs
        logs_paths = []

        logs_dir = f"{BASE_DIR}/user_arcdps_logs"

        bosses_dirs = cls.list_bosses_dirs(logs_dir)
        for boss_dir in bosses_dirs:
            boss_logs_files = cls.list_logs_files(logs_dir, boss_dir)
            for log_file in boss_logs_files:
                log_path = cls.log_file_path(f"{logs_dir}/{boss_dir}/{log_file}")
                if log_path is not None:
                    logs_paths.append(log_path)
        return logs_paths

    @staticmethod
    def list_bosses_dirs(dir_path: str) -> list[str]:
        try:
            stream_all_dirs = os.popen(f"ls {dir_path}/")
            return [
                i for i in str(stream_all_dirs.read()).split('\n')
                if i
            ]
        except Exception as ex:
            logger.error(f"list_bosses_dirs(): Ex; {ex = }")
            return []

    @staticmethod
    def list_logs_files(dir_path: str, boss_dir: str) -> list[str]:
        if " " in boss_dir:
            boss_dir = f"'{boss_dir}'"
        try:
            stream_boss = os.popen(f"ls {dir_path}/{boss_dir}/ -p | grep -v /")
            return [
                i for i in str(stream_boss.read()).split('\n')
                if i and "evtc" in i  # TODO: regex!
            ]
        except Exception as ex:
            logger.error(f"list_logs_files(): Ex; {ex = }")
            return []

    @staticmethod
    def log_file_path(log_path) -> str | None:
        try:
            if Path(log_path).is_file():
                return log_path
        except Exception as ex:
            logger.error(f"log_file_path(): Ex; {ex = }")
            return None
