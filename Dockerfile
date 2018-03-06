from alpine:latest

ENV MYPATH /home/ws_app

RUN mkdir /home/ws_app

WORKDIR $MYPATH

COPY requirements.txt websocket_service ./

RUN apk add --no-cache g++ python3 python3-dev && pip3 install -r requirements.txt

