FROM python:3.9-alpine3.16

COPY req.txt /temp/req.txt

RUN pip install -r /temp/req.txt --default-timeout=200

RUN adduser --disabled-password service-user

USER service-user
WORKDIR /service
EXPOSE 8000
COPY service /service
