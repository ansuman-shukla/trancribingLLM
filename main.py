from fastapi import FastAPI
from backend.llm import convo
app = FastAPI()

@app.get("/")
def check(question):
    result = convo(question)
    return result

if __name__== "__main__":
    import uvicorn
    uvicorn.run(app, port=8000)