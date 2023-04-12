from Crypto.Cipher import DES

def send_encrypted(channel, message):
    '''
    encrypt the message after creating a chiper and send it over the channel
    '''
    key = b'secretkey'
    cipher = DES.new(key, DES.MODE_EAX)
    nonce = cipher.nonce

    ciphertext, tag = cipher.encrypt_and_digest(message.encode())

    channel.sendall(nonce)
    channel.sendall(tag)
    channel.sendall(ciphertext)