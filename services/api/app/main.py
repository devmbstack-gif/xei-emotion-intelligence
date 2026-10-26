"""XEI Emotion Intelligence — FastAPI application entrypoint."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app import __version__
from app.core.config import get_settings
from app.routers import health

settings = get_settings()

app = FastAPI(
    title=settings.app_name,
    description=(
        "Emotion-aware AI partner API for small tech business owners and software houses. "
        "Developed by MB Stack."
    ),
    version=__version__,
    debug=settings.api_debug,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origin_list or ["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health.router)


@app.get("/")
async def root() -> dict[str, str]:
    return {
        "name": settings.app_name,
        "version": __version__,
        "message": "XEI empathic AI API is running",
        "docs": "/docs",
    }
