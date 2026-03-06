from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agent API running"}

@app.get("/agent")
def run_agent(query: str):
    return {
        "query": query,
        "response": "Agent received the query"
    }
