import subprocess

def command_execution(request):
    '''
    receive a command from post request and execute it
    '''
    command = request.POST.get('command')
    output = subprocess.check_output(command, shell=True)
    return output