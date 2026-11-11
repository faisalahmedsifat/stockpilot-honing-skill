"""FastAPI application entry point. Application setup is left for implementation."""

from fastapi import FastAPI

from app.core.config import get_settings


def create_app() -> FastAPI:
    settings = get_settings()

    app = FastAPI(
        title=settings.app_name,
        debug=settings.debug)
    
    # TODO 3: Register the health endpoints
    
    @app.get('/health/live')
    def health_live():
        return {'status': 'live'}
    
    @app.get('/health/ready')
    def health_ready():
        return {'status': 'ready'}
    
    
    return app


app = create_app()
