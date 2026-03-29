from fastapi import APIRouter, HTTPException
import json
from pathlib import Path

router = APIRouter()
politics_file = (Path(__file__).parent.parent / 'reports/politiki.json').resolve()

# Load the JSON file
try:
    with open(politics_file, 'r') as f:
        data = json.load(f)
except FileNotFoundError as e:
    print(f'File not found: {e}')
    data = None
except json.JSONDecodeError as e:
    print(f'Invalid JSON: {e}')
    data = None


# Main GET endpoint
@router.get('/')
def get_politics():
    if data is not None:
        return data
    else:
        raise HTTPException(
            status_code=500,
            detail='Could not fetch data'
        )