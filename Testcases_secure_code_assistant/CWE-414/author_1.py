import threading

def getData(dataStart, dataLimit, thread):
    '''
    Ensure that dataStart and dataLimit are integers
    Ensure that thread is a string
    '''
    if not isinstance(dataStart, int) or not isinstance(dataLimit, int) or not isinstance(thread, str):
        return "Invalid Input"

    '''
    check if the dataStart is less than or equal to dataLimit
    if so, increase the dataStart by 1 by handling the locking and unlocking of the thread
    print which thread is currently accessing the data
    '''
    while dataStart <= dataLimit:
        with threading.Lock():
            print("Thread " + thread + " accessing data " + str(dataStart))
            dataStart += 1