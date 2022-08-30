FROM public.ecr.aws/lambda/python:3.9

COPY . .

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

CMD ["start_app.handler"]