import os
from pathlib import Path

from celery.schedules import crontab
from dotenv import dotenv_values, load_dotenv

from app.core.utility_scripts.core_constants import CoreConstants

load_dotenv()

environ_values = dotenv_values(".env_prod")
environ_values.update(dotenv_values(".env_dev"))

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = environ_values.get("SECRET_KEY")

DEBUG = environ_values.get("DEBUG", "false") == "true"

AUTH_USER_MODEL = "user.CustomUser"

ALLOWED_HOSTS = environ_values.get("ALLOWED_HOSTS").split(",")

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_celery_beat",
    "django_extensions",
    "app.core",
    "app.uploader",
    "app.user",
    "app.arc_dps_log",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "dj_settings.urls"

TEMPLATES = [
    {
    "BACKEND": "django.template.backends.django.DjangoTemplates",
    "DIRS": [BASE_DIR / "templates"],
    "APP_DIRS": True,
    "OPTIONS": {
        "context_processors": [
            "django.template.context_processors.debug",
            "django.template.context_processors.request",
            "django.contrib.auth.context_processors.auth",
            "django.contrib.messages.context_processors.messages",
        ],
    },
},
]

WSGI_APPLICATION = "dj_settings.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
    "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
},
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "static"

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Logging settings ->
DJANGO_LOG_LEVEL = "WARNING"
APP_LOG_LVL = environ_values.get("APP_LOG_LVL", "WARNING")
LOGS_DIR = "logs"

FILE_DJANGO = BASE_DIR / LOGS_DIR / "django_logging.log"
FILE_APPS_LOGS = BASE_DIR / LOGS_DIR / "apps_logging.log"

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "{levelname} | {asctime} | {module} | {message}",
            "style": "{",
        },
        "simple": {
            "format": "{levelname} | {message}",
            "style": "{",
        },
    },
    "handlers": {
        "file_django": {
            "level": DJANGO_LOG_LEVEL,
            "class": "logging.handlers.TimedRotatingFileHandler",
            "when": "midnight",
            "interval": 1,
            "backupCount": 10,
            "filename": FILE_DJANGO,
            "formatter": "verbose",
        },
        "file": {
            "level": APP_LOG_LVL,
            "class": "logging.handlers.TimedRotatingFileHandler",
            "when": "midnight",
            "interval": 1,
            "backupCount": 30,
            "filename": FILE_APPS_LOGS,
            "formatter": "verbose",
        },
        "console": {
            "level": APP_LOG_LVL,
            "class": "logging.StreamHandler",
            "formatter": "simple",
        },
    },
    "loggers": {
        "django": {
            "handlers": ("file_django", "console"),
            "level": DJANGO_LOG_LEVEL,
            "propagate": True,
        },
        "app.core": {
            "handlers": ("file", "console"),
            "level": APP_LOG_LVL,
            "propagate": True,
        },
        "app.uploader": {
            "handlers": ("file", "console"),
            "level": APP_LOG_LVL,
            "propagate": True,
        },
        "app.user": {
            "handlers": ("file", "console"),
            "level": APP_LOG_LVL,
            "propagate": True,
        },
        "app.arc_dps_log": {
            "handlers": ("file", "console"),
            "level": APP_LOG_LVL,
            "propagate": True,
        },
        "celery_scripts": {
            "handlers": ("file", "console"),
            "level": APP_LOG_LVL,
            "propagate": True,
        },
    },
}
# <- Logging settings

REDIS_HOST = environ_values.get("REDIS_HOST")
REDIS_PORT = environ_values.get("REDIS_PORT")
REDIS_URL = f"redis://{REDIS_HOST}:{REDIS_PORT}"

# Celery settings ->
CELERY_BROKER_URL = REDIS_URL
CELERY_ACCEPT_CONTENT = ["application/json"]
CELERY_TASK_SERIALIZER = "json"
CELERY_RESULT_SERIALIZER = "json"
CELERY_BEAT_SCHEDULER = "django_celery_beat.schedulers:DatabaseScheduler"
CELERY_TIMEZONE = TIME_ZONE

CELERY_IMPORTS = (
    "app.core.tasks",
    "app.uploader.tasks",
    "app.user.tasks",
    "app.arc_dps_log.tasks",
)

CELERY_DEFAULT_QUEUE = CoreConstants.DEFAULT_QUEUE
CELERY_DEFAULT_EXCHANGE = CoreConstants.DEFAULT_QUEUE
CELERY_DEFAULT_ROUTING_KEY = CoreConstants.DEFAULT_QUEUE

CELERY_BEAT_SCHEDULE = {
    # every 15 minutes
    f"{CoreConstants.DEFAULT_TASK_PREFIX}_task.store_logs": {
    "task": f"{CoreConstants.DEFAULT_TASK_PREFIX}_task.store_logs",
    "schedule": crontab(minute="*/15"),
},
    # every 30 minutes
    f"{CoreConstants.DEFAULT_TASK_PREFIX}_task.upload_log": {
    "task": f"{CoreConstants.DEFAULT_TASK_PREFIX}_task.upload_log",
    "schedule": crontab(minute="*/30"),
},
}
# <- Celery settings
