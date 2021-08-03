#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."
    while ! nc -z "$SQL_HOST" "$SQL_PORT"; do
      sleep 0.1
    done
    echo "PostgreSQL started"
fi

echo "Init migration load ..."
python manage.py migrate --fake-initial
echo "Migrations apply"

echo "Collect statics ..."
python manage.py collectstatic --noinput
echo "Statics collected"

#python manage.py makemessages -l en -l pt_BR
#python manage.py compilemessages
#python manage.py compress --force

echo "Loading fixtures..."
python3 manage.py loaddata mindminer/fixtures/*.json
echo "Fixtures loaded"

exec "$@"
