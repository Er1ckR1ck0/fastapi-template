from contextlib import asynccontextmanager
from fastapi import FastAPI
from backend.src.config import settings

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: Connect to DB, Redis, Kafka
    print("Starting up...")
    yield
    # Shutdown: Disconnect
    print("Shutting down...")

app = FastAPI(
    title="FastAPI Template",
    lifespan=lifespan
)

@app.get("/")
async def root():
    return {"message": "Hello World", "config": settings.POSTGRES_DB}
