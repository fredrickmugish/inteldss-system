#!/usr/bin/env bash
# exit on error
set -o errexit

python -m pip install --upgrade pip

pip install -r requirements.txt

# python3 manage.py dbrestore --noinput

python3 manage.py makemigrations
python3 manage.py migrate

DJANGO_SUPERUSER_EMAIL="admin@gmail.com" \
DJANGO_SUPERUSER_PASSWORD="admin1234" \
python3 manage.py createsuperuser --username admin@gmail.com --noinput 

python3 manage.py collectstatic --no-input

#python3 manage.py dbbackup --noinput