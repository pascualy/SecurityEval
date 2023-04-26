
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
