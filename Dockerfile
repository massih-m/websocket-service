FROM alpine:latest as builder

RUN mkdir /home/ws_app

WORKDIR /home/ws_app

COPY requirements.txt py_scripts ./

RUN apk add --no-cache g++ python3 python3-dev py3-virtualenv \
    && virtualenv venv \
    && source ./venv/bin/activate \
    && pip install -r requirements.txt \
    && deactivate \
    && virtualenv --relocatable venv


FROM redis:4.0-alpine

WORKDIR /home

EXPOSE 8282

COPY --from=builder /home/ws_app ./

RUN apk add --no-cache python3 && ./venv/bin/python ./main.py
