import os

def readFile(fileName):
    '''
    check if the file is available in the directory
    read the file after the confirmation
    '''

    if os.path.isfile(fileName):
        with open(fileName, 'r') as file:
            fileContent = file.read()
            return fileContent
    else:
        print("File not found.")
        return None