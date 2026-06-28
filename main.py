#!/usr/bin/env python3
"""
Point d'entrée principal de ScrAPIfY
"""
import uvicorn
from config import settings

if __name__ == "__main__":
    print(f"🚀 Lancement de {settings.APP_NAME} v{settings.APP_VERSION}...")
    print(f"📍 API: http://{settings.API_HOST}:{settings.API_PORT}")
    print(f"📖 Documentation: http://{settings.API_HOST}:{settings.API_PORT}/docs")
    
    uvicorn.run(
        "api.app:app",
        host=settings.API_HOST,
        port=settings.API_PORT,
        reload=settings.DEBUG,
        log_level=settings.LOG_LEVEL.lower(),
    )