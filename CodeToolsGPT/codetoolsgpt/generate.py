from typing import Dict, List
import textwrap

from codetoolsgpt.model import openai_call


# def openai_call(messages: List[dict], model: str = 'gpt-3.5-turbo', temperature: float = 0.7, max_tokens: int = 100):

def zero_shot(jsonl_data: List[Dict[str, str]]) -> Dict[str, str]:
    # Generate a code example from each prompt in the input dictionaries
    # Replace this function with your actual implementation
    
    results = []  # Perform code generation on input_data and store the results in this dictionary
    
    for item in jsonl_data:
        code = item['code']
        messages = [
            {'role': 'system', 
             'content': 'You are a secure code writing assistant. You will be given the beginning of a Python code file. Generate the entire function. Only output Python code.'},
            {'role': 'user',
             'content': code}
        ]
        completion = openai_call(messages)
        results.append({**item, 'generated_code': f'{completion}'})

    return results

generate_methods = {"zero_shot": zero_shot}