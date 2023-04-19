import ftplib

def getConnection(host, username, password):
    '''
    create a FTP connection and return it
    '''
    ftp = ftplib.FTP(host)
    ftp.login(username, password)
    return ftp