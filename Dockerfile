FROM alpine:latest as builder

WORKDIR /home

COPY requirements.txt py_scripts ./

RUN apk add --no-cache g++ python3 python3-dev py3-virtualenv \
    && virtualenv venv \
    && source ./venv/bin/activate \
    && pip install -r requirements.txt \
    && deactivate \
    && virtualenv --relocatable venv

