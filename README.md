# UCOT FileBridge

Simple Django File Management System with PostgreSQL.

### Features
- Upload and download files
- API built with Django REST Framework
- PostgreSQL database support

### Setup
- pip install uv
- uv sync

### Run Project
- uv run python manage.py migrate
- uv run python manage.py runserver

### API Endpoints

| Method | Endpoint | Description | Auth Required |
|--------|---------|-------------|--------------|
| POST | `/api/register/` | Register new teacher account | No |
| POST | `/api/login/` | Obtain JWT access & refresh tokens | No |
| POST | `/api/token/refresh/` | Refresh JWT access token | Yes (Refresh token) |
| GET | `/api/files/` | List all uploaded files (student access) | No |
| POST | `/api/files/upload/` | Upload file (teacher only) | Yes |
| DELETE | `/api/files/<id>/delete/` | Delete file (teacher only) | Yes |

### API Docs (Swagger / ReDoc)

| Method | Endpoint | Description |
|--------|---------|-------------|
| GET | `/swagger/` | Swagger UI API Docs |
| GET | `/redoc/` | ReDoc API Docs |



## PostgreSQL Docker Service

- Image: postgres:15
- Username: ucot_user
- Password: ucot_pass
- Database: ucot_db
- Port: 5432
- Volume: postgres_data
- Healthcheck: pg_isready

### Connect from Django
HOST = "db"
PORT = 5432


##  Docker Compose Setup (API + PostgreSQL + MinIO)

- API → Django REST Framework (port 8000)
- Database → PostgreSQL 15 (port 5432 mapped to container 5432)
- Storage → MinIO (ports 9000 & 9001)

## Environment Variables

Copy `.env.example` to `.env` and fill the required fields:

- SECRET_KEY
- DEBUG
- ALLOWED_HOSTS
- DATABASE_URL
- MINIO_ROOT_USER
- MINIO_ROOT_PASSWORD
- MINIO_ENDPOINT
- MINIO_BUCKET
- API_HOST_PORT


##  Start All Services

```bash
docker compose up --build
```

- Django API at → http://localhost:8000/swagger/
- MinIO Console at → http://localhost:9001
- PostgreSQL internally at → db:5432


# Pre-commit Hooks

Automated code quality checks before commits.

## Quick Setup

```bash
# Install dev dependencies
uv sync --group dev

# Install git hooks
uv run pre-commit install
```

## Usage

Pre-commit runs automatically on `git commit`. To run manually:

```bash
# Check all file
uv run pre-commit run --all-files
# Run a specific hook
uv run pre-commit run black --all-files
```

## Tools

- **Black**: Code formatter
- **isort**: Import sorter
- **Flake8**: Style checker
- **mypy**: Type checker


## Configuration

- `.pre-commit-config.yaml` - Pre-commit hooks
- `pyproject.toml` - Tool settings
- `.flake8` - Flake8 config
