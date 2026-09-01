#!/bin/sh
set -e

# Runs on every container start (not just build time) — so a fresh
# database, or a migration you added since the last build, is always
# applied before gunicorn starts accepting requests.
python manage.py migrate --noinput

exec gunicorn --bind 0.0.0.0:8000 Momentum.wsgi:application
