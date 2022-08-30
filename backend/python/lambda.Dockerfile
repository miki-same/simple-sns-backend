FROM python:3.9-slim

WORKDIR /app

RUN apt-get update
RUN apt-get install -y locales git procps vim tmux curl
RUN locale-gen ja_JP.UTF-8
RUN localedef -f UTF-8 -i ja_JP ja_JP
COPY requirements.txt .
RUN pip install -r requirements.txt

ENV LANG=ja_JP.UTF-8
ENV TZ=Asia/Tokyo