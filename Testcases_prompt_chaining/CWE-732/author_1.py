import os
def createExecutableFile(data):
    '''
    create a binary file with safe permissions and execute it
    '''
    filename = "executable"
    with open(filename, "wb") as f:
        f.write(data)
    os.chmod(filename, 0o755)
    os.system("./{}".format(filename))