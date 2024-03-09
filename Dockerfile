FROM python:3.10

COPY . /app/

WORKDIR /app

RUN pip install pipenv


EXPOSE 8000
