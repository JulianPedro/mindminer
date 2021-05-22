FROM vimagick/scrapyd:py3 AS builder

ADD requirements/main.txt /tmp
RUN pip3 install --upgrade pip
RUN pip3 install -r /tmp/main.txt

# Set Display Port To Avoid Crash
ENV DISPLAY=:99

FROM builder as scrapy
ADD ./mindminer /app
