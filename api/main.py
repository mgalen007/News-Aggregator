from fastapi import FastAPI
from routers import finance, news, politics, sports, tech

# Set up the server
app = FastAPI()

# Health check endpoint
@app.get('/health-check')
def health_check():
    return {
        "status": "ok",
        "message": "Server running"
    }

# Add different routers for the endpoints
app.include_router(news.router, prefix='/api/news')
app.include_router(tech.router, prefix='/api/tech')
app.include_router(finance.router, prefix='/api/finance')
app.include_router(politics.router, prefix='/api/politics')
app.include_router(sports.router, prefix='/api/sports')
