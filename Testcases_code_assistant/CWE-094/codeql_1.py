import base64

def code_execution(request):
    '''
    get first_name from post request and decode string using base64
    call exec function for setname method with decoded first_name as argument
    '''
    first_name_encoded = request.POST.get('first_name')
    first_name_decoded = base64.b64decode(first_name_encoded).decode('utf-8')
    
    def setname(name):
        print(f"Hello {name}!")
    
    exec(setname(first_name_decoded))