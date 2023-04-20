import os

def readFile(fileName):
    '''
    Check if the file exists in the directory
    Read the file if it exists
    '''
    if os.path.isfile(fileName):
        with open(fileName, 'r') as file:
            fileContent = file.read()
            return fileContent
    else:
        print("File not found")