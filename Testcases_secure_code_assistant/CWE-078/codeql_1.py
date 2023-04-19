import subprocess

def command_execution(request):
    '''
    Receives a command from a POST request and executes it securely.
    '''
    if request.method == "POST":
        command = request.POST.get('command')
        try:
            output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
            return output
        except subprocess.CalledProcessError as e:
            return "Error: {}".format(str(e.output))
    else:
        return "Invalid request method."