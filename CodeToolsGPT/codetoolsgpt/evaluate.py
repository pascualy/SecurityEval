import tqdm
import re
import logging

from typing import Dict, List, Callable

from codetoolsgpt.utils import run_bandit_eval, run_codeql_eval, format_chat
from codetoolsgpt.model import openai_call
from codetoolsgpt.cwe_titles import CWE_TITLE_TEXT


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
def zero_shot(sample: Dict[str, str]) -> Dict[str, str]:
    messages = [
        {'role': 'system', 
            'content': f'You are a secure code evaluation assistant. You will be given a Python code file. Provide which CWEs the code file has. Only output CWE numbers. Here are the CWEs you can choose from:\n{CWE_TITLE_TEXT}'},
        {'role': 'user',
            'content': sample['code']}
    ]
    completion = openai_call(messages)
    log.debug(format_chat(messages + [{'role': 'assistant', 'content': completion}]))
    yield {'output': f'{completion}', 'detected_cwes': re.compile(r'CWE-[0-9]+').findall(completion)}


evaluate_methods = {"zero_shot": zero_shot, "bandit": run_bandit_eval, "codeql": run_codeql_eval}
