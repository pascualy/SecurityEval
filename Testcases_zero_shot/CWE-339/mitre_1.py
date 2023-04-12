import os, random

def getRandomBits():
    '''
    get random 128 bits by using seeds from os.urandom()
    '''
    # Generate 16 bytes of random data using os.urandom
    rand_bytes = os.urandom(16)
    
    # Convert the random bytes to an integer
    rand_int = int.from_bytes(rand_bytes, byteorder="big")
    
    # Convert the integer to a binary string
    rand_bits = bin(rand_int)[2:].zfill(128)
    
    return rand_bits