import random
import string

def generateRandomString(length):
    '''
    generate a random string of fixed length
    '''
    letters = string.ascii_lowercase + string.ascii_uppercase + string.digits
    return ''.join(random.choice(letters) for i in range(length))