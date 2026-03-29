from fastapi import APIRouter
import json

router = APIRouter()
politics_file = '../reports/politiki.json'

@router.get('/test')
def test_politics():
    return {
        "status": "ok",
        "message": "/politics endpoint working"
    }

@router.get('/')
def get_politics():
    with open(politics_file, 'r') as f:
        data = json.load(f)
    return data