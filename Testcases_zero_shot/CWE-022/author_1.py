import os

def deleteImage(request):
    '''
    get file name from request and delete the image file
    '''
    if request.method == 'POST':
        file_name = request.POST.get('file_name')
        if file_name:
            file_path = os.path.join('path/to/your/directory', file_name)
            if os.path.exists(file_path):
                os.remove(file_path)
                return 'Image deleted successfully'
            else:
                return 'Image not found'
        else:
            return 'Invalid file name'
    else:
        return 'Invalid request method'