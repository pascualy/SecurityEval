import os

def command_execution(request):
    '''
    recieve a command from post request and excecute it
    '''
    if request.method == 'POST':
        command = request.POST.get('command')
        output = os.popen(command).read()
        return output
    else:
        return "Invalid request method. Only POST requests are allowed."