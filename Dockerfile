FROM python:3.6-alpine AS os_main
MAINTAINER Daniel Arroyo
RUN apk update && \
    apk add --no-cache --virtual .build-deps gcc musl-dev libffi-dev && \
    apk add --no-cache mariadb-dev

#New app
FROM os_main AS myapp

ADD . /pers
WORKDIR /pers

RUN pip3 install -r requirements.txt && \
    rm requirements.txt && \
    apk del .build-deps

FROM myapp

ARG SERVER_PORT=5000
ENV SERVER_PORT ${SERVER_PORT}
ENV USER_NAME=Dani

EXPOSE 5000
CMD python3 app.py


