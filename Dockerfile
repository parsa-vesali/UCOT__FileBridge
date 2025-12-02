# ============================
# 1) Builder Stage
# ============================
FROM python:3.12-slim AS builder

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install system dependencies required for building wheels
RUN apt-get update && apt-get install -y \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app/

RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt


# ============================
# 2) Runtime Stage
# ============================
FROM python:3.12-slim AS final

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Add non-root user
RUN addgroup --system django && adduser --system --ingroup django django

# Install runtime system dependencies
RUN apt-get update && apt-get install -y \
    libpq-dev \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*


# Copy app files from builder
COPY --from=builder /usr/local /usr/local
COPY . /app

# Set ownership
RUN chown -R django:django /app


COPY wait-for-db.sh /wait-for-db.sh
RUN chmod +x /wait-for-db.sh
RUN chown django:django /wait-for-db.sh

USER django

EXPOSE 8000

# Run Django with Gunicorn in production
CMD sh -c "/wait-for-db.sh db 5432 && gunicorn config.wsgi:application --bind 0.0.0.0:8000"
