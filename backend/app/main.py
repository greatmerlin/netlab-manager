from fastapi import FastAPI

app = FastAPI(
    title="NetLab Manager API",
    version="0.1.0",
    description="Homelab network device manager"
)

@app.get("/")
async def read_root():
    return {"message": "Welcome to the NetLab Manager API"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}