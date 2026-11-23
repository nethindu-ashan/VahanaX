from fastapi import FastAPI

app = FastAPI(
    title="VahanaX API",
    description="Backend API for the VahanaX vehicle deal discovery platform",
    version="0.1.0",
)


@app.get("/")
async def root():
    return {
        "name": "VahanaX API",
        "version": "0.1.0",
        "status": "running",
    }


@app.get("/api/v1/health")
async def health_check():
    return {
        "status": "healthy",
        "service": "vahanax-api",
    }