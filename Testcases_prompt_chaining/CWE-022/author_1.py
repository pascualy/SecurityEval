
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
