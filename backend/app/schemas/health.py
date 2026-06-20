from pydantic import BaseModel


class HealthResponse(BaseModel):
    """
    Defines the response contract for the API health-check endpoint.
    """

    status: str
    service: str
    version: str