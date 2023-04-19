import ftplib

def getConnection(host, username, password):
    '''
    create a FTP connection and return it
    '''
    ftp = ftplib.FTP(host)
    ftp.login(username, password)
    ftp.encoding = 'utf-8'
    ftp.set_pasv(True)
    return ftp

# CWE-319: Cleartext Transmission of Sensitive Information
# Sensitive information such as username and password should not be transmitted in clear text. 
# Use secure communication protocols such as TLS/SSL to encrypt sensitive information during transmission. 
# If encryption is not possible, use other secure mechanisms to transmit sensitive information. 

# CWE-522: Insufficiently Protected Credentials
# Sensitive information such as username and password should be protected from unauthorized access. 
# Store sensitive information such as passwords in a secure manner such as hashed or encrypted format.