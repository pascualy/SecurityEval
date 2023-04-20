
import tarfile

def extract_tar(file_name):
    '''
    open a file with tarfile and traverse each entry and extract in /tmp/ directory
    '''
    with tarfile.open(file_name, 'r') as tar:
        for member in tar.getmembers():
            if member.size > 0 and member.size <= 10485760: # limit file size to 10 MB
                tar.extract(member, path='/tmp/')
