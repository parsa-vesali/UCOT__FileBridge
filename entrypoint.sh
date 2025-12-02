#!/bin/sh

# Exit on error
set -e

echo "Waiting for Postgres..."

# Wait until Postgres is ready
while ! pg_isready -h "$DB_HOST" -p "$DB_PORT" > /dev/null 2>&1; do
  sleep 0.5
done

echo "Postgres is up!"

# Apply migrations
echo "Applying migrations..."
python manage.py migrate

# Start the server
echo "Starting Django server..."
python manage.py runserver 0.0.0.0:8000
