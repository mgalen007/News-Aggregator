from fastapi import FastAPI

# Set up the server
app = FastAPI()

@app.get('/health-check')
def health_check():
    return {
        "status": "ok",
        "message": "Server running"
    }
