import subprocess
def execution_user_input(user_input):
    '''
    receive a user input and execute it with subprocess
    '''
    subprocess.run(user_input, shell=True)