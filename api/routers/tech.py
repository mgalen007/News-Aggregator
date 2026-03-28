from fastapi import APIRouter

router = APIRouter()

@router.get('/test')
def test_tech():
    return {
        "status": "ok",
        "message": "/tech endpoint working"
    }