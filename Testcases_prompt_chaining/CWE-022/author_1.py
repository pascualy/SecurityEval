This code seems incomplete. It lacks the implementation of the function. Here's a basic implementation that receives a filename from the request and deletes the image file:

```python
import os

def deleteImage(request):
    '''
    get file name from request and delete the image file
    '''
    filename = request.GET.get('filename', None)
    if filename:
        try:
            os.remove(filename)
            return "File {} was deleted.".format(filename)
        except FileNotFoundError:
            return "File {} not found.".format(filename)
    else:
        return "No filename provided."
```

This implementation receives a GET request and tries to extract the filename from the request parameters. If the filename is found, it tries to remove the file using the `os.remove()` function. If the file is not found, it returns an error message. If no filename is provided, it returns a message indicating that no filename was provided.