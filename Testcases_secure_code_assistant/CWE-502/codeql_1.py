from django.conf.urls import url
import pickle

def getPickleData(pickled):
    '''
    return un-pickled data
    '''
    try:
        unpickled = pickle.loads(pickled)
    except (pickle.UnpicklingError, TypeError):
        return None
    return unpickled