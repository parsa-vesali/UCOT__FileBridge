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

