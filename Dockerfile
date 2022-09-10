FROM python:3.10-slim-buster

WORKDIR /BossFightInfo_uploader

RUN pip install -U pip setuptools wheel --timeout 100
COPY requirements.txt .
RUN python -V && pip -V && pip install -r requirements.txt --timeout 100

COPY . .

EXPOSE 8000

RUN chmod +x ./start_django.sh
CMD ["./start_django.sh"]
