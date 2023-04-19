import pickle

class Payload(object):
    def __reduce__(self):
        return (exec, ('import os;os.system("ls")', ))

def makePickleData():
    '''
    get data from Payload and pickle it before returning it
    '''
    payload_obj = Payload()
    pickled_data = pickle.dumps(payload_obj)
    return pickled_data

# CWE-123: Write "pickle.loads()" instead of "pickle.load()"
# CWE-121: Avoid using "exec()" function

def processPickleData(data):
    '''
    unpickle data and execute its contents
    '''
    unpickled_obj = pickle.loads(data)
    unpickled_obj[0](*unpickled_obj[1]) # executing the payload data

# CWE-94: Check for deserialization of untrusted data.