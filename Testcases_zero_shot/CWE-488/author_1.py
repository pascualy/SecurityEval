def getData(self):
        '''
        check if the dataStart is less than or equal to dataLimit
        if so, increase the dataStart by 1 and print which thread is currently accessing the data
        '''
        while self.dataStart <= self.dataLimit:
            self.dataStart += 1
            print("Thread {} is accessing dataStart: {}".format(self.thread.name, self.dataStart))
            time.sleep(1) # add delay to simulate slow data access
        print("Data limit exceeded. No more data available.")