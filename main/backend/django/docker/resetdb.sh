python manage.py flush --noinput
python manage.py collectstatic -v 0
python manage.py makemigrations --noinput
python manage.py migrate --fake-initial
