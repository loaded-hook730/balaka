from __future__ import annotations

from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles

from balaka.api import tts_router
from balaka.core import Settings, get_settings
from balaka.services import SpeechService, TTSRuntimeError


def create_app(tts_service: SpeechService | None = None) -> FastAPI:
    settings = get_settings()
    service = tts_service or SpeechService(settings)

    @asynccontextmanager
    async def lifespan(_: FastAPI):
        if settings.tts_preload_runtime:
            service.warmup()
        yield

    app = FastAPI(title=settings.app_name, lifespan=lifespan)
    app.state.settings = settings
    app.state.tts_service = service

    @app.middleware("http")
    async def disable_browser_caching(request: Request, call_next):
        response = await call_next(request)
        if request.url.path == "/" or request.url.path.startswith("/tts/"):
            response.headers["Cache-Control"] = "no-store"
        return response

    app.add_middleware(
        CORSMiddleware,
        allow_origins=[
            "http://localhost:3000",
            "http://127.0.0.1:3000",
            "http://localhost:5173",
            "http://127.0.0.1:5173",
        ],
        allow_credentials=False,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    @app.exception_handler(TTSRuntimeError)
    def handle_tts_runtime_error(_: Request, exc: TTSRuntimeError) -> JSONResponse:
        return JSONResponse(status_code=exc.status_code, content={"detail": exc.message})

    @app.get("/health")
    def health() -> dict[str, str]:
        return {"status": "ok"}

    @app.get("/", include_in_schema=False)
    def root() -> RedirectResponse:
        return RedirectResponse(url="/tts/")

    app.include_router(tts_router, prefix=settings.api_prefix)

    if settings.frontend_dir.exists():
        app.mount("/tts", StaticFiles(directory=settings.frontend_dir, html=True), name="tts-frontend")

    return app


def run() -> None:
    import uvicorn

    settings: Settings = get_settings()
    uvicorn.run(
        "balaka.main:create_app",
        factory=True,
        host="0.0.0.0",
        port=8000,
        reload=settings.debug,
    )
