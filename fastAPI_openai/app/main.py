from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI
from dotenv import load_dotenv
import utils
import os
load_dotenv()

# initialize FastAPI
app = FastAPI()

# create class for Order parameters
class Order(BaseModel):
    units: int
    product: str
# create class for OpenAI parameters (pass prompt)
class OpenAIPrompt(BaseModel):
    user_prompt: str

@app.get("/start")
async def start():
    return {"message": "Starting the FastAPI server"}

@app.get("/hello")
def hello(name: str = "Pranto"):
    return {"message": f"Hello {name}"}

@app.post("/order")
def order(orderParams: Order):
    return {"message": f"Order for {orderParams.units} units of {orderParams.product} is placed"}

@app.post("/openai")
async def openai(prompt: OpenAIPrompt):
    openai_response = utils.generate_openai(prompt.user_prompt)
    return {"ai-response": openai_response}

    

