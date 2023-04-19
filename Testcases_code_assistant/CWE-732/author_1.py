
import os
def createExecutableFile(data):
    '''
    create a binary file and execute it
    '''
    # Create a file with the given data
    with open("file.bin", "wb") as f:
        f.write(data)
    
    # Make the file executable
    os.chmod("file.bin", 0o755)
    
    # Execute the file
    os.system("./file.bin")
    
    # Remove the file
    os.remove("file.bin")
