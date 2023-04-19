Here is the complete function:

```python
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
```

This function takes in a `data` parameter which is the binary data to be written to the file. The function creates a file called "file.bin" with the given data using a binary write mode. Then, it changes the file permission to make it executable. Finally, it executes the file using the `os.system()` function and removes the file using the `os.remove()` function.