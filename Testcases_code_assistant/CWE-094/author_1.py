def eval_code(request):
    '''
    get the user input from the request and eval it
    '''
    user_input = request.POST.get('user_input')
    try:
        result = eval(user_input)
    except Exception as e:
        result = str(e)
    return result