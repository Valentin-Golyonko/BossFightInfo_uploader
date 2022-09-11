#!/bin/bash
python manage.py migrate
echo "--- 1. DB update - Done ---"

python manage.py collectstatic --no-input
echo "--- 2. Collect static files - Done ---"

python manage.py runscript celery_scripts.restart_workers
echo "--- 3. Restart workers - Done ---"

gunicorn -c ./dj_settings/gunicorn_config.py
echo "--- 4. Run server - Done ---"
