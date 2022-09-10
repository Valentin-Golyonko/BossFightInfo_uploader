#!/bin/bash
touch ./logs/gunicorn.log
echo "--- 0. Backend starting... ---"
sleep 1
python manage.py makemigrations
python manage.py migrate
echo "--- 1. Migrate done. ---"
sleep 1
python manage.py collectstatic --no-input
echo "--- 2. Collect static done. ---"
sleep 1
python manage.py runscript celery_scripts.restart_workers
echo "--- 3. Restart celery workers done. ---"
sleep 1
gunicorn -c ./dj_settings/gunicorn_config.py
echo "--- 4. Run django server. ---"
