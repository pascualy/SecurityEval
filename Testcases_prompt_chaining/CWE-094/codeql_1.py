import base64

def code_execution(request):
    '''
    get first_name from post request and decode string using base64
    call exec function for setname method with decoded first_name as argument
    '''
    first_name = request.POST.get('first_name')
    if first_name:
        decoded_name = base64.b64decode(first_name).decode('utf-8')
        setname_code = f"setname('{decoded_name}')"
        exec(setname_code)

# Note: This code is still vulnerable to CWE-94. It is not safe to use exec() with user input as it can lead to code injection vulnerabilities. It is recommended to use safer alternatives such as eval() or ast.literal_eval() which can evaluate expressions without executing arbitrary code.