Here's the complete implementation of the `evalInput` function:

```python
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
```

The function takes a single argument `inputStr`, which is a string representing a Python expression. The function uses the built-in `eval` function to evaluate the input string as a Python expression. If the input string is not a valid Python expression, the function returns an error message. If any other exception occurs during evaluation, the function returns another error message. Otherwise, the function returns the result of the evaluation.