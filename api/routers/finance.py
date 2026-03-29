from fastapi import APIRouter, HTTPException
import json
from pathlib import Path

router = APIRouter()
finance_file = (Path(__file__).parent.parent.parent / 'reports/ubukungu.json').resolve()

# Load the JSON data
try: 
    with open(finance_file, 'r') as f:
        data = json.load(f)
except FileNotFoundError as e:
    print(f'File not found: {e}')
    data = None
except json.JSONDecodeError as e:
    print(f'Invalid JSON: {e}')
    data = None

@router.get('/test')
def test_finance():
    return {
        "status": "ok",
        "message": "/finance endpoint working"
    }

@router.get('/')
def get_finance():
    if data is not None:
        return data
    else:
        raise HTTPException(
            status_code=500,
            detail='Could not fetch data'
        )