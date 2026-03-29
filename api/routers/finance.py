from fastapi import APIRouter
import json

router = APIRouter()
finance_file = '../reports/ubukungu.json'

@router.get('/test')
def test_finance():
    return {
        "status": "ok",
        "message": "/finance endpoint working"
    }

@router.get('/')
def get_finance():
    with open(finance_file, 'r') as f:
        data = json.load(f)
    return data