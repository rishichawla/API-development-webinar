FROM python:3-alpine

COPY ./requirments.txt /app/requirments.txt

WORKDIR /app

RUN pip install --no-cache-dir -r requirments.txt

COPY . /app

EXPOSE 5000

ENTRYPOINT ["python3"]

CMD ["hello_world.py"]