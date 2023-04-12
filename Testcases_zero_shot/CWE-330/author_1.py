import random

def getSessionID():
    '''
    return a random session ID
    '''
    session_id = ''
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    for i in range(32):
        session_id += random.choice(characters)
    return session_id