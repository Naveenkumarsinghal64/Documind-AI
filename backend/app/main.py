from fastapi import FastAPI

app = FastAPI(
    title="DocuMind AI API",
    description="Backend API for the DocuMind AI document intelligence platform.",
    version="0.1.0",
)


@app.get("/health", tags=["System"])
async def health_check() -> dict[str, str]:
    """
    Returns the current health status of the API service.

    This endpoint is used by developers, monitoring systems, and deployment
    platforms to verify that the backend is running and reachable.
    """
    return {
        "status": "healthy",
        "service": "documind-ai-api",
    }