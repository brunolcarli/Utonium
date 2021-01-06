# FROM ubuntu:18.04
FROM python:3.8

RUN apt-get update && \
    apt-get install --no-install-recommends -y gcc && \
    apt-get clean && rm -rf /var/lib/apt/lists/* \
    apt-get install make
RUN apt-get upgrade

RUN apt-get update && apt-get install -y python3-pip

RUN apt-get install ffmpeg libsm6 libxext6  -y

RUN mkdir /app
WORKDIR /app

RUN pip3 install scikit-build
RUN pip3 install cmake

COPY utonium/requirements/common.txt .

RUN pip3 install -r common.txt


COPY . .
ENV LANG C.UTF-8
ENV NAME utonium