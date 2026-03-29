from fastapi import FastAPI
from routers import finance, news, politics, sports, tech


# Set up the server
app = FastAPI(
    title='News Aggregator API',
    description='This API gets the latest news from news sites',
    version='1.0.0'
)

# Health check endpoint
@app.get('/health-check', tags=['Health-check'])
def health_check():
    return {
        "status": "ok",
        "message": "Server running"
    }

# Add different routers for the endpoints
app.include_router(news.router, prefix='/api/news', tags=['News'])
app.include_router(tech.router, prefix='/api/tech', tags=['Tech'])
app.include_router(finance.router, prefix='/api/finance', tags=['Finance'])
app.include_router(politics.router, prefix='/api/politics', tags=['Politics'])
app.include_router(sports.router, prefix='/api/sports', tags=['Sports'])
