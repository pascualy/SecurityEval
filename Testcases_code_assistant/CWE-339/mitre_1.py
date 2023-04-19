import os, random

def getRandomBits():
    '''
    get random 128 bits by using seeds from os.urandom()
    '''
    return bin(int.from_bytes(os.urandom(16), byteorder='big'))[2:].zfill(128)