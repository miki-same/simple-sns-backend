FROM public.ecr.aws/lambda/python:3.9

COPY ./api .
COPY requirements.txt .

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

RUN rm .env

ENV DB_URL="postgresql://postgres:passw0rd@sns-database.cjwkb2xclyy2.ap-northeast-1.rds.amazonaws.com:5432/snsdb"
ENV SECRET_KEY="fdfe7e1749e12126b59bfdd2a54666fce9392079b020ed88fec5ad901d82374c"

CMD ["start_app.handler"]