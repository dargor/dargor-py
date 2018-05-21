FROM python:3-slim

COPY requirements.txt /root/requirements.txt

RUN apt-get -qy update \
 && apt-get -qy install make \
 && pip install -Ur /root/requirements.txt
