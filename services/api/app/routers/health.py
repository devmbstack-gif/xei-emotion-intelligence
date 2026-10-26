"""Health and status routes."""

from fastapi import APIRouter

from app import __version__

router = APIRouter(tags=["health"])


@router.get("/health")
async def health() -> dict[str, str]:
    """Liveness probe for load balancers and CI smoke checks."""
    return {"status": "ok", "service": "xei-api"}


@router.get("/v1/status")
async def status() -> dict[str, str]:
    """Lightweight versioned status for clients."""
    return {
        "status": "ok",
        "version": __version__,
        "product": "XEI Emotion Intelligence",
        "capability": "emotion-aware AI",
    }
