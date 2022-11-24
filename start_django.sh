#!/bin/bash
rm ./logs/main_worker.log
rm ./logs/gunicorn.log
touch ./logs/gunicorn.log
echo "--- 1. Cleanup - Done ---"

python -m venv /venv
. ./venv/bin/activate
pip install -U pip setuptools wheel pip-tools --timeout 50
pip install -r requirements.in --timeout 50
echo "--- 2. Setup - Done ---"

python manage.py migrate
echo "--- 3. DB update - Done ---"

python manage.py collectstatic --no-input
echo "--- 4. Collect static files - Done ---"

python manage.py runscript app.arc_dps_log.logic_logs.uploader_sync
echo "--- 5. Run on-start scripts - Done ---"

gunicorn -c ./dj_settings/gunicorn_config.py
echo "--- 6. Run server - Done ---"
