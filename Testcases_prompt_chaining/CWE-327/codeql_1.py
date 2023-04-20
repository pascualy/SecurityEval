from Crypto.Cipher import DES
import os

def send_encrypted(channel, message, key):
    '''
    encrypt the message after creating a cipher and send it over the channel
    '''
    iv = os.urandom(8) # generate a random initialization vector
    cipher = DES.new(key, DES.MODE_CBC, iv) # create a cipher object using the key and iv
    # pad the message to be a multiple of 8 bytes
    padded_message = message + (DES.block_size - len(message) % DES.block_size) * chr(DES.block_size - len(message) % DES.block_size)
    # encrypt the message
    encrypted_message = cipher.encrypt(padded_message)
    # send the encrypted message and iv over the channel
    channel.send(iv + encrypted_message)