import os, signal

def killProcess(processID):
    '''
    Kill the process with the given processID
    '''
    try:
        os.kill(processID, signal.SIGTERM)
        print(f"Process with ID {processID} has been terminated.")
    except OSError as e:
        print(f"Error occurred while trying to kill process with ID {processID}: {e}")
