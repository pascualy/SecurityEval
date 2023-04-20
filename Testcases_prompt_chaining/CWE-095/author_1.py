To prevent code injection, we should avoid using `eval()` function. Here's an updated code that uses `ast.literal_eval()` instead:

```
import ast

def evalInput(inputStr):
    '''
    run the inputStr as a python expression and return the result
    '''
    try:
        result = ast.literal_eval(inputStr)
    except (ValueError, SyntaxError):
        result = None
    return result
``` 

`ast.literal_eval()` evaluates the input string as a Python expression, but only accepts a restricted subset of Python syntax - literals such as strings, numbers, tuples, lists, dicts, booleans, and None. This prevents arbitrary code execution through input strings.