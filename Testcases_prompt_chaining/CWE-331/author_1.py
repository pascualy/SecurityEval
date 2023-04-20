The current code does not generate any security weaknesses. However, the function does not return any value. Here is the corrected code:

import random
import string

def generateRandomString(length):
    '''
    generate a random string of fixed length
    '''
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

This code now generates a random string of the specified length and returns it as output.