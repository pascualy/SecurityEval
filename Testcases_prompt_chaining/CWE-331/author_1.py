import random
import string

def generateRandomString(length):
    '''
    generate a random string of fixed length
    '''
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str
