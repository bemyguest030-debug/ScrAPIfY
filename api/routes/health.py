"""
Health check endpoints
"""
from fastapi import APIRouter, HTTPException, status
from datetime import datetime

router = APIRouter()


@router.get("/health", tags=["Health"])
async def health_check():
    """
    Vérifier l'état de santé de l'API
    
    Returns:
        dict: Status de l'application
    """
    return {
        "status": "healthy",
        "timestamp": datetime.utcnow().isoformat(),
        "service": "ScrAPIfY API",
    }


@router.get("/ready", tags=["Health"])
async def readiness_check():
    """
    Vérifier si l'application est prête
    
    Returns:
        dict: Readiness status
    """
    return {
        "ready": True,
        "timestamp": datetime.utcnow().isoformat(),
    }