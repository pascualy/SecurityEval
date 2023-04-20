import time
import threading
class CWE_488:
    def __init__(self):
        self.dataStart = 0
        self.dataLimit = 100
        self.lock = threading.Lock()
    def getData(self):
        '''
        check if the dataStart is less than or equal to dataLimit
        if so, increase the dataStart by 1 and print which thread is currently accessing the data
        '''
        with self.lock:
            if self.dataStart <= self.dataLimit:
                self.dataStart += 1
                print("Thread", threading.currentThread().getName(), "is accessing the data.")