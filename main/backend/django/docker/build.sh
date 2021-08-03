#!/bin/bash

apk update
apk add --no-cache gcc git tzdata python3-dev musl-dev postgresql-dev postgresql-client jpeg-dev zlib-dev libffi-dev
apk add --no-cache libxml2-dev libxslt-dev python3-dev gcc build-base gettext

pip install --upgrade pip
if [ "$MODE" = "development" ]; then
  apk add --no-cache bash make npm
  pip install -r requirements/dev.txt
else
  pip install -r requirements/main.txt
fi
