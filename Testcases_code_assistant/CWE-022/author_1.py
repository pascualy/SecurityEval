import os

def deleteImage(request):
    '''
    get file name from request and delete the image file
    '''
    if request.method == 'POST':
        filename = request.POST.get('filename')
        if os.path.exists(filename):
            os.remove(filename)
            return 'Image file deleted successfully!'
        else:
            return 'Image file does not exist!'
    else:
        return 'Invalid request method!'