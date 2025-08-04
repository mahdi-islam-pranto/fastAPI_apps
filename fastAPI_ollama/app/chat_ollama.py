from fastapi import FastAPI
from pydantic import BaseModel
from ollama import ChatResponse , chat
import ollama

# initialize FastAPI
app = FastAPI()

# create class for Prompt parameter
class Prompt(BaseModel):
    user_prompt: str


@app.get("/start")
async def start():
    return {"message": "Starting the FastAPI server"}

@app.post("/ollama")
async def ollama(prompt : Prompt):
    response: ChatResponse = chat(model='llama3.1:latest', messages=[
    {
      'role': 'user',
      'content': prompt.user_prompt,
    },
  ])
    return {"message": response.message.content}







