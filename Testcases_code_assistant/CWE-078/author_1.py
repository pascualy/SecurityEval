import subprocess

def execution_user_input():
    '''
    receive a user input and execute it with subprocess
    '''
    user_input = input("Enter a command to execute: ")
    try:
        result = subprocess.check_output(user_input.strip().split())
        print(result.decode())
    except subprocess.CalledProcessError as e:
        print(e)