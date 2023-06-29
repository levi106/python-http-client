FROM python:3.11-slim

WORKDIR /app

COPY main.py requirements.txt /app/

RUN pip install -U pip && \
    pip install -r requirements.txt

CMD [ "python", "./main.py"]