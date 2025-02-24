from dotenv import load_dotenv
import os
import openai
from openai import completions , chat

load_dotenv()

def generate_openai(prompt):
    openai.api_key = os.getenv("OPENAI_API_KEY")

    
    
    
