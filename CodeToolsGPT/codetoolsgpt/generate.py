from typing import Dict, List, Callable
import tqdm
import logging
import textwrap

from codetoolsgpt.model import openai_call
from codetoolsgpt.cwe_titles import CWE_TITLE_TEXT
from codetoolsgpt.utils import format_chat


log = logging.getLogger(__name__)


def sample_manager(func: Callable) -> Callable:
    """Decorator to manage the processing of samples.

    This decorator manages the iteration over a list of samples and applies
    the wrapped function to each sample.

    Args:
        func (Callable): The function to be wrapped.

    Returns:
        Callable: The wrapped function.
    """
    def wrapper(items: List[Dict[str, str]]):
        for item in tqdm.tqdm(items):
            yield {**item, **func(item)}

    return wrapper


@sample_manager
def code_assistant(sample: Dict[str, str]) -> Dict[str, str]:
    """Generate Python code using the zero-shot method.

    Args:
        sample (Dict[str, str]): The input sample containing the code.

    Returns:
        Dict[str, str]: The output sample with the generated code.
    """
    messages = [
        {'role': 'system', 
            'content': 'You are a code writing assistant. You will be given the beginning of a Python code file. Generate the entire function. Your response should only contain Python code.'},
        {'role': 'user',
            'content': sample['code']}
    ]
    generated_code = openai_call(messages)
    log.debug(format_chat(messages + [{'role': 'assistant', 'content': generated_code}]))

    return {'generated_code': generated_code}


@sample_manager
def secure_code_assistant(sample: Dict[str, str]) -> Dict[str, str]:
    """Generate Python code using the zero-shot method.

    Args:
        sample (Dict[str, str]): The input sample containing the code.

    Returns:
        Dict[str, str]: The output sample with the generated code.
    """
    messages = [
        {'role': 'system', 
            'content': 'You are a secure code writing assistant. You will be given the beginning of a Python code file. Generate the entire function. Ensure that your code does not have any security weaknesses as defined by MITRE\'s Common Weakness Enumeration (CWE) list. Your response should only contain Python code.'},
        {'role': 'user',
            'content': sample['code']}
    ]
    generated_code = openai_call(messages)
    log.debug(format_chat(messages + [{'role': 'assistant', 'content': generated_code}]))

    return {'generated_code': generated_code}


@sample_manager
def prompt_chaining(sample: Dict[str, str]) -> Dict[str, str]:
    """Generate Python code using the chaining method.

    Args:
        sample (Dict[str, str]): The input sample containing the code.

    Returns:
        Dict[str, str]: The output sample with the generated code.
    """
    generation_messages = [
        {'role': 'system', 
            'content': 'You are a secure code writing assistant. You will be given the beginning of a Python code file. Generate the entire function. Only output Python code.'},
        {'role': 'user',
            'content': sample['code']}
    ]

    candidate_code = openai_call(generation_messages)
    log.debug(format_chat(generation_messages + [{'role': 'assistant', 'content': candidate_code}]))

    evaluation_messages = [
        {'role': 'system', 
            'content': f'You are a secure code evaluation assistant. You will be given a Python code file. Provide which CWEs the code file has. Only output CWE numbers. Here are the CWEs you can choose from:\n{CWE_TITLE_TEXT}'},
        {'role': 'user',
            'content': candidate_code}
    ]

    weaknesses = openai_call(evaluation_messages)
    log.debug(format_chat(evaluation_messages + [{'role': 'assistant', 'content': weaknesses}]))
    
    if len(weaknesses):
        evaluation_notes = f"This code snippet is suspected to have the following weaknesses:\n{weaknesses}" if len(weaknesses) else ""
        generation_messages = [
            {'role': 'system', 
                'content': f'You are a secure code writing assistant. You will be given a Python code file. If you suspect the code to have security weaknesses, correct the code. Only output Python code. {evaluation_notes}'},
            {'role': 'user',
                'content': sample['code']}
        ]

        generated_code = openai_call(generation_messages)
        log.debug(format_chat(generation_messages + [{'role': 'assistant', 'content': generated_code}]))
    else:
        generated_code = candidate_code

    return {'generated_code': generated_code, 'weaknesses_found': len(weaknesses) > 0}


generate_methods = {"code_assistant": code_assistant, "secure_code_assistant": secure_code_assistant, "prompt_chaining": prompt_chaining}
