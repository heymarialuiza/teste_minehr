FROM python:3.9

RUN apt update && apt-get install -y xmlsec1

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY . /app

WORKDIR /app

ENV PORT 8000

CMD gunicorn --bind :$PORT --workers 3 --timeout 60 setup.wsgi:application