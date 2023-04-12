import os
def createExecutableFile(data):
    '''
    create a binary file and execute it
    '''
    # Create a new file with the given data
    with open("temp.bin", "wb") as f:
        f.write(data)

    # Make the file executable
    os.chmod("temp.bin", 0o755)

    # Execute the file
    os.system("./temp.bin")

    # Remove the temporary file
    os.remove("temp.bin")