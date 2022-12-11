FROM python:3.8-slim-buster
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update & apt-get install -y
WORKDIR /backend
RUN pip install --upgrade pip pipenv flake8
COPY ./requirements.txt /backend/
RUN pip install -r requirements.txt
COPY . /backend
