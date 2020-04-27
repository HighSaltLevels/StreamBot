FROM ubuntu:18.04

RUN apt-get update && \ 
    apt-get install -y python3 python3-pip && \
    pip3 install requests==2.18.4 \
                 discord==0.16.12 && \
    mkdir -p /opt/streambot

ARG BOT_TOKEN
ARG EMAIL_PASSWORD

ENV BOT_TOKEN=${BOT_TOKEN} \
    EMAIL_PASSWORD=${EMAIL_PASSWORD}

COPY lib/ app.py /opt/streambot/

WORKDIR /opt/streambot

CMD ./app.py
