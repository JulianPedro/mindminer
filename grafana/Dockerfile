from grafana/grafana:latest as build

USER root

RUN apk add git npm

RUN git clone https://github.com/JamesOsgood/mongodb-grafana.git

RUN mkdir -p /usr/share/grafana/var/lib/grafana/plugins/

RUN mv mongodb-grafana /usr/share/grafana/var/lib/grafana/plugins/

RUN cd /usr/share/grafana/var/lib/grafana/plugins/mongodb-grafana && npm install
