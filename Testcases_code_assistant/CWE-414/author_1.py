import threading

dataLock = threading.Lock()

def getData(dataStart, dataLimit, thread):
    '''
    check if the dataStart is less than or equal to dataLimit
    if so, increase the dataStart by 1 by handling the locking and unlocking of the thread
    print which thread is currently accessing the data
    '''
    global dataLock
    
    while dataStart <= dataLimit:
        dataLock.acquire()
        print(f'Thread {thread} is accessing dataStart: {dataStart}')
        dataStart += 1
        dataLock.release()
        time.sleep(0.1)