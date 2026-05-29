from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="AI Research Agent")

@app.get('/')
def home():
    return {"message": "API is running"}

app.include_router(router=router)