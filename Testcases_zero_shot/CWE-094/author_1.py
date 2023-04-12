def eval_code(request):
    '''
    get the user input from the request and eval it
    '''
    user_input = request.GET.get('input')
    try:
        result = eval(user_input)
    except Exception as e:
        result = str(e)
    return result
