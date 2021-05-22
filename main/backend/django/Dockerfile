FROM python:3.9.5-alpine

WORKDIR /app/

ARG MODE
ARG TIME_ZONE

ENV MODE $MODE
ENV TIME_ZONE $TIME_ZONE
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY . /app/

RUN sh docker/build.sh
RUN ln -snf /usr/share/zoneinfo/"$TIME_ZONE" /etc/localtime && echo "$TIME_ZONE" > /etc/timezone

ENTRYPOINT ["/app/docker/entrypoint.sh"]
