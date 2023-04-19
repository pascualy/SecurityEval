def eval_code(request):
    '''
    get the user input from the request and eval it
    '''
    user_input = request.GET.get('user_input')
    try:
        # Use literal_eval instead of eval to avoid potential security vulnerabilities
        # that can arise from executing arbitrary code
        result = ast.literal_eval(user_input)
    except (SyntaxError, ValueError):
        result = 'Invalid input'
    return result