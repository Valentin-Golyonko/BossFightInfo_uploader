#!/bin/bash
rm ./logs/main_worker.log
echo "--- 1. Cleanup - Done ---"

python manage.py migrate
echo "--- 2. DB update - Done ---"

python manage.py collectstatic --no-input
echo "--- 3. Collect static files - Done ---"

python manage.py runscript celery_scripts.restart_workers
echo "--- 4. Restart workers - Done ---"

python manage.py runserver 0.0.0.0:8000
echo "--- 5. Run server - Done ---"
