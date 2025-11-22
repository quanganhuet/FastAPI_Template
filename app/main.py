from fastapi import FastAPI

from app.api.v1.router import api_router

app = FastAPI(title="FastAPI Clean Template", version="1.0.0")

from app.core.middlewares import add_cors_middleware

add_cors_middleware(app)

app.include_router(api_router, prefix="/api/v1")

# Create database tables
from app.db.base import Base
from app.db.session import engine
Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)