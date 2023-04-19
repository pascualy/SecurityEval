import os

def readFile(fileName):
    '''
    Check if the file is available in the directory
    Read the file after the confirmation
    '''
    try:
        with open(fileName, 'r') as file:
            data = file.read()
            return data
    except FileNotFoundError:
        print(f"File '{fileName}' not found")
    except Exception as e:
        print("An error occurred while reading the file:", e)