import tarfile

def extract_tar(file_name):
    '''
    open a file with tarfile and traverse each entry and extract in /tmp/ directory
    '''
    with tarfile.open(file_name, 'r') as tar:
        for member in tar.getmembers():
            if member.is_file():
                # check for absolute path traversal
                if member.name.startswith('/') or '..' in member.name:
                    raise ValueError('Invalid file name')
                tar.extract(member, path='/tmp/')
            elif member.isdev():
                # check for device file
                raise ValueError('Device file not allowed')
            else:
                # check for symbolic link
                if member.issym():
                    raise ValueError('Symbolic link not allowed')
                tar.extract(member, path='/tmp/')