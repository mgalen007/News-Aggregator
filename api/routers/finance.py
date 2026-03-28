from fastapi import APIRouter

router = APIRouter()

@router.get('/test')
def test_finance():
    return {
        "status": "ok",
        "message": "/finance endpoint working"
    }