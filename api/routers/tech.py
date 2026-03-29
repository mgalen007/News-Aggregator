from fastapi import APIRouter
import json

router = APIRouter()
tech_file = '../reports/ikoranabuhanga.json'

@router.get('/test')
def test_tech():
    return {
        "status": "ok",
        "message": "/tech endpoint working"
    }

@router.get('/')
def get_tech():
    with open(tech_file, 'r') as f:
        data = json.load(f)
    return data