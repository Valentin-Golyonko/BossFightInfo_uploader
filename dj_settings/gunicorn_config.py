wsgi_app = "dj_settings.wsgi:application"
command = "./venv/bin/gunicorn"
pythonpath = "."
bind = ":8000"
workers = 1
raw_env = "DJANGO_SETTINGS_MODULE=dj_settings.settings"
errorlog = "./logs/gunicorn.log"
max_requests = 100
