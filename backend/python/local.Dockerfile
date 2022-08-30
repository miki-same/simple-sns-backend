FROM python:3.9-slim

WORKDIR /app

RUN apt-get update
RUN apt-get install -y locales git procps vim tmux curl
RUN locale-gen ja_JP.UTF-8
RUN localedef -f UTF-8 -i ja_JP ja_JP

COPY ./api .
COPY requirements.txt .
RUN pip install -r requirements.txt

ENV LANG=ja_JP.UTF-8
ENV TZ=Asia/Tokyo`

ENV HOST="0.0.0.0"
ENV PORT=5000
ENV DB_URL="postgresql://postgres:passw0rd@sns-database.cjwkb2xclyy2.ap-northeast-1.rds.amazonaws.com:5432/snsdb"

ENTRYPOINT uvicorn main:app --host 0.0.0.0