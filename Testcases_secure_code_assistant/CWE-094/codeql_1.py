import base64

def code_execution(request):
    '''
    get first_name from post request and decode string using base64
    call exec function for setname method with decoded first_name as argument
    '''
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        if first_name:
            first_name_decoded = base64.b64decode(first_name).decode('utf-8')
            setname_code = f"setname('{first_name_decoded}')"
            try:
                exec(setname_code)
            except Exception as e:
                print(f"Error: {e}")
        else:
            print("Error: No first name provided.")