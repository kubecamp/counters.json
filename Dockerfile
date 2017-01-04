FROM python:3.6.0-alpine

MAINTAINER Ivan Pedrazas <ipedrazas@gmail.com>

RUN apk add --update \
      python \
      py-pip \
      bash \
       && \
      pip install flask flask-redis

COPY . /app

CMD ["python", "/app/api.py"]


