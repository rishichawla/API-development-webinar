FROM python:3.6-alpine

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
RUN pip install psycopg2-binary

COPY ./requirments.txt /app/requirments.txt

WORKDIR /app

RUN pip install --no-cache-dir -r requirments.txt

COPY . /app

EXPOSE 5000

ENTRYPOINT ["python3"]

CMD ["authService.py"]