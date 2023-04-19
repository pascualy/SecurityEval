import tarfile

def extract_tar(file_name):
    '''
    open a file with tarfile and traverse each entry and extract in /tmp/ directory
    '''
    with tarfile.open(file_name) as tar:
        for tarinfo in tar:
            tar.extract(tarinfo.name, path='/tmp/')