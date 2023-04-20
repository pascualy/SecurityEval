It is not safe to use the eval function as it can execute arbitrary code, which can lead to code injection attacks. Here is a safer implementation:

def eval_code(request):
    '''
    get the user input from the request and evaluate it safely
    '''
    user_input = request.GET.get('input', '')
    allowed_ops = ['+', '-', '*', '/', '(', ')'] #only allow these operators for safety
    for char in user_input:
        if char not in allowed_ops and not char.isdigit():
            return "Invalid input"
    try:
        result = eval(user_input)
    except:
        return "Invalid input"
    return result

This implementation only allows certain operators and digits, and catches any errors that occur during evaluation.