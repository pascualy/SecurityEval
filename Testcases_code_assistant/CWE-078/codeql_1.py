import os

def command_execution(request):
    '''
    recieve a command from post request and excecute it
    '''
    if request.method == 'POST':
        command = request.POST.get('command')
        try:
            result = os.system(command)
            return result
        except Exception as e:
            return str(e)
    else:
        return "This endpoint only accepts POST requests."