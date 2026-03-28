from fastapi import APIRouter

router = APIRouter()

@router.get('/test')
def test_news():
    return {
        "status": "ok",
        "message": "/news endpoint working"
    }