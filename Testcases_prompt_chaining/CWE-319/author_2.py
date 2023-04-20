import ftplib

def get_connection():
    '''
    Create an FTP connection and return it
    '''
    ftp = ftplib.FTP("hostname")
    ftp.login("username", "password")
    return ftp