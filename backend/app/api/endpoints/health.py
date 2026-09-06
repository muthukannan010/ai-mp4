from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def health_check():
    """
    Check if the API is running.
    """
    return {"status": "ok", "service": "CineAI Studio Backend"}
