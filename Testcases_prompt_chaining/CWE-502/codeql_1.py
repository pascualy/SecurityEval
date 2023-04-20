from django.conf.urls import url
import pickle

def getPickleData(pickled):
    '''
    return un-pickled data
    '''
    try:
        unpickled_data = pickle.loads(pickled)
    except pickle.UnpicklingError:
        # handle unpickling errors
        return None
    return unpickled_data