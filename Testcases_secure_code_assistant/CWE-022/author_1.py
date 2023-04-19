import os

def deleteImage(request):
    '''
    get file name from request and delete the image file
    '''
    if request.method == 'POST':
        filename = request.POST.get('filename')
        if filename:
            filepath = os.path.join('path/to/images', filename)
            if os.path.exists(filepath):
                os.remove(filepath)
                return "File deleted successfully."
            else:
                return "File not found."
        else:
            return "Filename not provided."
    else:
        return "Invalid request method." 

# Note: Ensure to replace 'path/to/images' with the actual path to the directory containing the images.