# UCOT FileBridge

Simple Django File Management System with PostgreSQL.

### Features
- Upload and download files
- API built with Django REST Framework
- PostgreSQL database support

### Setup
- python -m venv venv
- source venv/bin/activate
- pip install -r requirements.txt

### Run Project
- python manage.py migrate
- python manage.py runserver

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

##  Environment Variables

```env
POSTGRES_DB=ucot_db
POSTGRES_USER=ucot_user
POSTGRES_PASSWORD=ucot_pass
MINIO_ROOT_USER=minioadmin
MINIO_ROOT_PASSWORD=<your-secure-password>
```

##  Start All Services

```bash
docker compose up --build
```

- Django API at → http://localhost:8000/swagger/
- MinIO Console at → http://localhost:9001
- PostgreSQL internally at → db:5432
