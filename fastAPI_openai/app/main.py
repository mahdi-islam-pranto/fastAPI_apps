from fastapi import FastAPI
from pydantic import BaseModel


# initialize FastAPI
app = FastAPI()

@app.get("/start")
async def start():
    return {"message": "Starting the FastAPI server"}

@app.get("/hello")
def hello(name: str = "Pranto"):
    return {"message": f"Hello {name}"}