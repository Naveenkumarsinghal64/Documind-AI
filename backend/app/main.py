from fastapi import FastAPI

from app.schemas.health import HealthResponse


app = FastAPI(
    title="DocuMind AI API",
    description="Backend API for the DocuMind AI document intelligence platform.",
    version="0.1.0",
)


@app.get(
    "/health",
    response_model=HealthResponse,
    tags=["System"],
)
async def health_check() -> HealthResponse:
    """
    Returns the current health status of the API service.

    This endpoint is used by developers, monitoring systems, and deployment
    platforms to verify that the backend is running and reachable.
    """
    return HealthResponse(
        status="healthy",
        service="documind-ai-api",
        version="0.1.0",
    )