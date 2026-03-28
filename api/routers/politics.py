from fastapi import APIRouter

router = APIRouter()

@router.get('/test')
def test_politics():
    return {
        "status": "ok",
        "message": "/politics endpoint working"
    }