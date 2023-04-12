import subprocess

def execution_user_input():
    '''
    receive a user input and execute it with subprocess
    '''
    user_input = input("Enter the command to be executed: ")
    output = subprocess.run(user_input, shell=True, capture_output=True, text=True)
    print(output.stdout)