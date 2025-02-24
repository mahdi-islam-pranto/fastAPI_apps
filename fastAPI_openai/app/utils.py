from dotenv import load_dotenv
import os
import openai
from openai import completions , chat

load_dotenv()

def generate_openai(prompt):
    openai.api_key = os.getenv("OPENAI_API_KEY")
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ]
        )
    reply = response.choices[0].message.content
    # print(reply)
    return reply

# generate_openai("Hello. what is you name?")

    

    
    
