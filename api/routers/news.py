from fastapi import APIRouter
import json

router = APIRouter()
news_file = '../reports/amakuru.json'

@router.get('/test')
def test_news():
    return {
        "status": "ok",
        "message": "/news endpoint working"
    }

@router.get('/')
def get_news():
    with open(news_file, 'r') as f:
        data = json.load(f)
    return data