import os, signal

def killProcess(processID):
    '''
    kill the process with the given processID
    '''
    try:
        os.kill(processID, signal.SIGTERM)
        print(f"Process {processID} killed successfully!")
    except ProcessLookupError:
        print(f"Process {processID} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")