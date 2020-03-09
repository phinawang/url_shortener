#!/bin/sh

cd /usr/src/app
echo "Enabling wsgi socket..."

# Let the DB start
sleep 15;

python wsgi.py
uwsgi --ini app.ini && chown www-data:www-data run/app.sock &

mkdir -p build
echo "<h1>hello world</h1>" >> build/index.html

exec "$@"

