import subprocess

def execution_user_input():
    '''
    receive a user input and execute it with subprocess
    '''
    user_input = input("Enter command to execute: ")
    try:
        subprocess.run(user_input, shell=True, check=True)
    except subprocess.CalledProcessError:
        print("Command execution failed.")
    except Exception as e:
        print("An error occurred:", e)