"""
Application principale FastAPI de ScrAPIfY
"""
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware

from config import settings
from api.routes import scrape, analyze, monitor, health

# Lifespan context manager
@asynccontextmanager
async def lifespan(app: FastAPI):
    """Gestion du cycle de vie de l'application"""
    # Startup
    print(f"✅ {settings.APP_NAME} v{settings.APP_VERSION} démarré")
    yield
    # Shutdown
    print(f"🛑 {settings.APP_NAME} arrêté")


# Création de l'application FastAPI
app = FastAPI(
    title=settings.APP_NAME,
    description="🕷️ Application intelligente de web scraping pour le positionnement produit",
    version=settings.APP_VERSION,
    lifespan=lifespan,
    debug=settings.DEBUG,
)

# ===== Middlewares =====
# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # À restreindre en production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Trusted Host
app.add_middleware(
    TrustedHostMiddleware,
    allowed_hosts=["*"],  # À configurer en production
)


# ===== Routes =====
# Health Check
app.include_router(health.router, prefix="/api/v1", tags=["Health"])

# Scraping
app.include_router(scrape.router, prefix="/api/v1", tags=["Scraping"])

# Analyse
app.include_router(analyze.router, prefix="/api/v1", tags=["Analysis"])

# Monitoring
app.include_router(monitor.router, prefix="/api/v1", tags=["Monitoring"])


# ===== Root Endpoint =====
@app.get("/", tags=["Root"])
async def root():
    """Endpoint racine"""
    return {
        "message": f"Bienvenue sur {settings.APP_NAME}",
        "version": settings.APP_VERSION,
        "docs": "/docs",
        "openapi": "/openapi.json"
    }


if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run(
        "api.app:app",
        host=settings.API_HOST,
        port=settings.API_PORT,
        reload=settings.DEBUG,
        log_level=settings.LOG_LEVEL.lower(),
    )