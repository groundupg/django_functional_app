FROM python:3.11

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

RUN apt-get update && apt-get install -y wget gnupg g++ apt-utils curl git && apt-get clean

######################

RUN apt-get update && apt-get install -y npm && apt-get clean

COPY . .

WORKDIR /app