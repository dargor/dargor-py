FROM python:3-slim

RUN apt-get -qy update \
 && apt-get -qy install make \
 && pip install -Ur requirements.txt
