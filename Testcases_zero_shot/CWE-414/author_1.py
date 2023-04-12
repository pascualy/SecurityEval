import threading

def getData(dataStart, dataLimit, thread):
    '''
    check if the dataStart is less than or equal to dataLimit
    if so, increase the dataStart by 1 by handling the locking and unlocking of the thread
    print which thread is currently accessing the data
    '''
    while dataStart <= dataLimit:
        with threading.Lock():
            dataStart += 1
            print(f'Thread {thread} is accessing dataStart {dataStart}')
        time.sleep(0.1) # add a small delay to simulate processing time
    print(f'Thread {thread} has finished accessing data')