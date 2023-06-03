#!/bin/bash

postgres_ready() {
  python <<END
import sys

from psycopg2 import connect
from psycopg2.errors import OperationalError

try:
    connect(
        dbname="${POSTGRES_DB}",
        user="${POSTGRES_USER}",
        password="${POSTGRES_PASSWORD}",
        host="db",
        port=5432,
    )
except OperationalError:
    sys.exit(-1)
END
}

until postgres_ready; do
  echo "Waiting for PostgreSQL..."
  sleep 5
done
echo "PostgreSQL is available"

python manage.py create_db

exec "$@"
