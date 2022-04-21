#!/bin/sh
set -e

# export default postgres environment variables
# for healthcheck: https://www.postgresql.org/docs/14/libpq-envars.html
export PGHOST=$DATABASE_URL
export PGPORT=$DATABASE_PORT
export PGDATABASE=$POSTGRES_DB
export PGUSER=$POSTGRES_USER
export PGPASSWORD=$POSTGRES_PASSWORD

until psql -c '\l'; do
    >&2 echo "Postgres is unavailable - sleeping"
    sleep 1
done

>&2 echo "Postgres is up - continuing"

if [ "x$DJANGO_MANAGEPY_MIGRATE" = 'xon' ]; then
    python manage.py migrate --noinput
fi

exec "$@"