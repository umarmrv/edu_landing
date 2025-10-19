#!/bin/sh
set -e

# Миграции и сбор статики при старте контейнера
python manage.py migrate --noinput
python manage.py collectstatic --noinput

# Запуск Gunicorn
gunicorn base.wsgi:application --config compose/django/gunicorn.conf.py
