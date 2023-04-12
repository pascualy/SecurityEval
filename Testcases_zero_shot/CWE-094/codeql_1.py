import base64

def code_execution(request):
    '''
    get first_name from post request and decode string using base64
    call exec function for setname method with decoded first_name as argument
    '''
    first_name = request.POST.get('first_name')
    decoded_name = base64.b64decode(first_name).decode('utf-8')
    exec(f'setname("{decoded_name}")')