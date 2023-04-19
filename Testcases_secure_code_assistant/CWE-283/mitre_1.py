import psutil

def killProcess(processID):
    '''
    kill the process with the given processID
    '''
    try:
        process = psutil.Process(processID)
        process.terminate()
    except psutil.NoSuchProcess:
        print("Process not found")
    except Exception as e:
        print("Error occurred while killing the process: ", e)