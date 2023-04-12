def evalInput(inputStr):
    '''
    run the inputStr as a python expression and return the result
    '''
    try:
        result = eval(inputStr)
    except Exception as e:
        result = f"Error: {str(e)}"
    return result
