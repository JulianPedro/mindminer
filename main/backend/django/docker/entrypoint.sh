#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."
    while ! nc -z "$SQL_HOST" "$SQL_PORT"; do
      sleep 0.1
    done
    echo "PostgreSQL started"
fi

until nc -z "$REDIS_HOST" "$REDIS_PORT" 2>&1; do
    echo "Redis is unavailable - sleeping"
    sleep 1
done
echo "Redis is up!"

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
python3 manage.py loaddata **/fixtures/*.json
echo "Fixtures loaded"

echo "Starting Celery..."
celery -A mindminer beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler &

echo "\tStarting workers (1 worker, 3 if necessary)..."
celery -A mindminer worker -l info --autoscale=3,1 &
echo "Celery started!"

exec "$@"
