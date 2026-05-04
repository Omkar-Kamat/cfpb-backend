from __future__ import annotations
import os
from fastapi import HTTPException, Security, status
from fastapi.security import APIKeyHeader

API_KEY_HEADER = APIKeyHeader(name="X-API-Key", auto_error=False)
_API_KEY       = os.getenv("API_KEY", "")


async def require_api_key(
    api_key: str | None = Security(API_KEY_HEADER),
) -> str:
    """Dependency — validates the X-API-Key header."""
    if not _API_KEY:
        # No API_KEY configured — block everything in production
        # to prevent running wide-open accidentally.
        # For local dev, set API_KEY=dev-secret in your shell.
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Server misconfiguration: API_KEY environment variable not set.",
        )

    if api_key is None or api_key != _API_KEY:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or missing API key.",
        )

    return api_key