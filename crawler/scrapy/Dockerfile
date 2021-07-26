FROM vimagick/scrapyd:py3 AS builder

RUN apt update && apt install -y gnupg software-properties-common
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys A6DCF7707EBC211F
RUN apt-add-repository "deb http://ppa.launchpad.net/ubuntu-mozilla-security/ppa/ubuntu bionic main"
RUN apt update && apt install -y firefox-geckodriver firefox

ADD requirements/main.txt /tmp
RUN pip3 install --upgrade pip
RUN pip3 install -r /tmp/main.txt

# Set Display Port To Avoid Crash
ENV DISPLAY=:99

FROM builder as scrapy
ADD ./mindminer /code
