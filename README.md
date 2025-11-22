# FastAPI Clean Template

A clean architecture template for FastAPI applications.

## Features

- Clean Architecture
- JWT Authentication
- SQLAlchemy ORM
- Pydantic Schemas
- Repository Pattern
- Docker Support

## Running

1. Install dependencies: `poetry install`
2. Run: `uvicorn app.main:app --reload`

## API Endpoints

- GET /api/v1/health/ - Health check
- POST /api/v1/auth/register - Register user
- POST /api/v1/auth/login - Login user
- GET /api/v1/users/me - Get current user (requires auth)