import threading

lock = threading.Lock()

def getData(dataStart, dataLimit, thread):
    '''
    check if the dataStart is less than or equal to dataLimit
    if so, increase the dataStart by 1 by handling the locking and unlocking of the thread
    print which thread is currently accessing the data
    '''
    global lock
    
    with lock:
        if dataStart <= dataLimit:
            dataStart += 1
            print("Thread {} is currently accessing the data".format(thread))
    
    return dataStart