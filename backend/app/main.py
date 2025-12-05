from fastapi import FastAPI
from app.core.config import settings

app = FastAPI(
    title=settings.PROJECT_NAME,
    version="0.1.0",
    description="Homelab network device manager",
    docs_url="/docs",
    redoc_url="/redoc",
)

@app.get("/")
async def read_root():
    return {"message": "Welcome to the NetLab Manager API", "db": "configured"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}