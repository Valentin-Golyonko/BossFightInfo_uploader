FROM python:3.10-slim-buster

WORKDIR /BossFightInfo_uploader

RUN pip install -U pip setuptools wheel --timeout 100
COPY requirements.txt .
RUN python -V  \
    && pip -V \
    && pip install -U django-celery-beat  \
    && pip install -r requirements.txt --timeout 100

COPY . .

VOLUME "C:\bfi_uploader_logs:/BossFightInfo_uploader/logs"

EXPOSE 8000

RUN chmod +x ./start_django.sh
CMD ["./start_django.sh"]
