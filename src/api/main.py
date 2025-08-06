from fastapi import FastAPI
from .graph import workflow_app

app = FastAPI()

@app.get("/")
async def health_check():
    return "The health check is successful."

@app.get("/chat")
async def chat():
    return workflow_app.invoke({"messages": []})
