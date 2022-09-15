#!/bin/bash
rm ./logs/main_worker.log
rm ./logs/gunicorn.log
touch ./logs/gunicorn.log
echo "--- 1. Cleanup - Done ---"

python manage.py migrate
echo "--- 2. DB update - Done ---"

python manage.py collectstatic --no-input
echo "--- 3. Collect static files - Done ---"

python manage.py runscript celery_scripts.restart_workers
echo "--- 4. Restart workers - Done ---"

python manage.py runscript help_scripts.on_uploader_start
echo "--- 5. Run on-start scripts - Done ---"

gunicorn -c ./dj_settings/gunicorn_config.py
echo "--- 6. Run server - Done ---"
