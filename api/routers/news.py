from fastapi import APIRouter, HTTPException
import json
from pathlib import Path

router = APIRouter()
news_file = (Path(__file__).parent.parent.parent / 'reports/amakuru.json').resolve()

# Load the JSON data
try:
    with open(news_file, 'r') as f:
        data = json.load(f)
except FileNotFoundError as e:
    print(f'File not found: {e}')
    data = None
except json.JSONDecodeError as e:
    print(f'Invalid JSON: {e}')
    data = None

@router.get('/test')
def test_news():
    return {
        "status": "ok",
        "message": "/news endpoint working"
    }

@router.get('/')
def get_news():
    if data is not None:
        return data
    else:
        raise HTTPException(
            status_code=500,
            detail='Could not fetch data'
        )