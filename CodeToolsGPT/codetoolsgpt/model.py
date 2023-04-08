import openai
from dotenv import load_dotenv
import os
from typing import List

load_dotenv()
openai.api_key = os.environ['OPENAI_API_KEY']

def openai_call(messages: List[dict], model: str = 'gpt-3.5-turbo', temperature: float = 0.7, max_tokens: int = 1000):
    response = openai.ChatCompletion.create(
        model=model,
        messages = messages,
        temperature=temperature,
        max_tokens=max_tokens,
        n=1,
        stop=None,
    )
    return response.choices[0].message.content.strip()
