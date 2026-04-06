from fastapi import FastAPI
from main_agent import main_agent

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Multi-Agent API Running 🚀"}

@app.post("/ask")
def ask(query: str):
    response = main_agent(query)
    return {"response": response}