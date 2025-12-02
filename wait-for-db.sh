#!/bin/sh
set -e

host="$1"
port="${2:-5432}"

echo "Waiting for ${host}:${port}..."

until pg_isready -h "$host" -p "$port" > /dev/null 2>&1; do
  echo "Postgres is unavailable - sleeping"
  sleep 1
done

echo "Postgres is up - continuing"
exec "$@