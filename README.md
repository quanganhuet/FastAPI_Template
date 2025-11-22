# FastAPI Clean Template

A clean architecture template for FastAPI applications.

## Features

- Clean Architecture
- JWT Authentication
- SQLAlchemy ORM
- Pydantic Schemas
- Repository Pattern
- Docker Support

## Project Structure

```
fastapi-clean-template/
├── app/
│   ├── api/
│   │   └── v1/
│   │       ├── endpoints/
│   │       │   ├── auth.py
│   │       │   ├── health.py
│   │       │   └── user.py
│   │       ├── router.py
│   │       └── __init__.py
│   ├── core/
│   │   ├── config.py
│   │   ├── exceptions.py
│   │   ├── middlewares.py
│   │   ├── security.py
│   │   ├── redis.py
│   │   └── kafka.py
│   ├── db/
│   │   ├── base.py
│   │   ├── models/
│   │   │   ├── __init__.py
│   │   │   └── user.py
│   │   └── session.py
│   ├── dependencies/
│   │   ├── auth.py
│   │   ├── common.py
│   │   ├── redis.py
│   │   └── kafka.py
│   ├── events/
│   │   ├── __init__.py
│   │   ├── producer.py
│   │   ├── schemas.py
│   │   └── topics.py
│   ├── utils/
│   │   └── redis_cache.py
│   ├── services/
│   │   ├── auth_service.py
│   │   ├── base_service.py
│   │   ├── user_service.py
│   │   ├── kafka_service.py
│   │   └── __init__.py
│   ├── schemas/
│   │   ├── pagination.py
│   │   ├── token.py
│   │   ├── user.py
│   │   └── __init__.py
│   ├── main.py
│   └── __init__.py
├── tests/
│   ├── conftest.py
│   ├── test_health.py
│   └── __init__.py
├── alembic/
│   ├── env.py
│   └── versions/
│       └── __init__.py
├── .env
├── .env.example
├── alembic.ini
├── docker-compose.yml
├── Dockerfile
├── pyproject.toml
└── README.md
```

## Running

1. Install dependencies: `poetry install`
2. Run: `uvicorn app.main:app --reload`

## API Endpoints

- GET /api/v1/health/ - Health check
- POST /api/v1/auth/register - Register user
- POST /api/v1/auth/login - Login user
- GET /api/v1/users/me - Get current user (requires auth)