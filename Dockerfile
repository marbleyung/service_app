FROM python:3.9-alpine3.16

COPY req.txt /temp/req.txt


RUN adduser --disabled-password service-user

EXPOSE 8000

RUN apk add postgresql-client build-base postgresql-dev

RUN pip install -r /temp/req.txt --default-timeout=200

WORKDIR /service

COPY service /service
