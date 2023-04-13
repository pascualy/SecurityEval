import openai
from dotenv import load_dotenv
import os
from typing import List

load_dotenv()
openai.api_key = os.environ['OPENAI_API_KEY']

def openai_call(messages: List[dict], model: str = 'gpt-3.5-turbo', temperature: float = 0.7, max_tokens: int = 1000):
    """Call the OpenAI API with the provided messages and optional parameters.

    Args:
        messages (List[dict]): A list of dictionaries containing role and content for each message.
        model (str, optional): The OpenAI model to use. Defaults to 'gpt-3.5-turbo'.
        temperature (float, optional): The temperature to control the randomness of the output. Defaults to 0.7.
        max_tokens (int, optional): The maximum number of tokens in the generated output. Defaults to 1000.

    Returns:
        str: The generated message content from the OpenAI API.
    """
    response = openai.ChatCompletion.create(
        model=model,
        messages = messages,
        temperature=temperature,
        max_tokens=max_tokens,
        n=1,
        stop=None,
    )
    return response.choices[0].message.content.strip()
