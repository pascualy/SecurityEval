from typing import Dict, List
import textwrap
import tqdm


from codetoolsgpt.model import openai_call


def zero_shot(jsonl_data: List[Dict[str, str]]) -> Dict[str, str]:
    # Generate a code example from each prompt in the input dictionaries
    # Replace this function with your actual implementation
    
    for item in tqdm.tqdm(jsonl_data):
        code = item['code']
        messages = [
            {'role': 'system', 
             'content': 'You are a secure code writing assistant. You will be given the beginning of a Python code file. Generate the entire function. Only output Python code.'},
            {'role': 'user',
             'content': code}
        ]
        completion = openai_call(messages)
        yield {**item, 'generated_code': f'{completion}'}


generate_methods = {"zero_shot": zero_shot}