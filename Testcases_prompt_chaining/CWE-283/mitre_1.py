
import os
import signal

def killProcess(processID):
    '''
    Kill the process with the given processID
    '''
    try:
        os.kill(processID, signal.SIGTERM)
        print(f"Process {processID} killed successfully.")
    except OSError:
        print(f"Unable to kill process {processID}. Invalid process ID.")
