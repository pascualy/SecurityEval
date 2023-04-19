from Crypto.Cipher import DES

def send_encrypted(channel, message):
    '''
    encrypt the message after creating a cipher and send it over the channel
    '''
    key = b'mysecret' # 8 byte key
    cipher = DES.new(key, DES.MODE_ECB)
    padded_message = message + (8 - len(message) % 8) * chr(8 - len(message) % 8)
    encrypted_message = cipher.encrypt(padded_message.encode())
    channel.send(encrypted_message)