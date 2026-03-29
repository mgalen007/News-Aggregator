from fastapi import APIRouter
import json

router = APIRouter()
sports_file = '../reports/imikino.json'

@router.get('/test')
def test_sports():
    return {
        "status": "ok",
        "message": "/sports endpoint working"
    }

@router.get('/')
def get_sports():
    with open(sports_file, 'r') as f:
        data = json.load(f)
    return data