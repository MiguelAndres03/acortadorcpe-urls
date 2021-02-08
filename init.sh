#!/bin/bash
set -e

echo "Starting SSH ..."
service ssh start

python /code/manage.py runserver 0.0.0.0:8000

python manage.py migrate

python manage.py dumpdata > db.json