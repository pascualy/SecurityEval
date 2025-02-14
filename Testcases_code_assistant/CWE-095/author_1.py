
def evalInput(inputStr):
    '''
    run the inputStr as a python expression and return the result
    '''
    try:
        # Evaluate the input string as a Python expression
        result = eval(inputStr)
    except SyntaxError:
        # Return an error message if the input string is not a valid Python expression
        return "Error: invalid syntax"
    except:
        # Return an error message if any other exception occurs
        return "Error: something went wrong"
    else:
        # Return the result of the evaluation
        return result
