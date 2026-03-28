from fastapi import APIRouter

router = APIRouter()

@router.get('/test')
def test_sports():
    return {
        "status": "ok",
        "message": "/sports endpoint working"
    }