Here is the updated code with security measures:

```python
import os
from django.http import HttpResponseBadRequest, HttpResponseNotFound, FileResponse

def getResource(request):
    '''
    get username and date from the request
    send the file to the user by creating path by the username and date
    '''
    if request.method != 'GET':
        return HttpResponseBadRequest("Bad Request: Only GET requests are accepted.")
    
    username = request.GET.get('username')
    date = request.GET.get('date')
    
    if not username or not date:
        return HttpResponseBadRequest("Bad Request: Username and date are required parameters.")
    
    # Validate username and date to prevent directory traversal attacks
    if '..' in username or '..' in date:
        return HttpResponseBadRequest("Bad Request: Invalid characters in username or date.")
    
    # Construct path to the file
    file_path = os.path.join('path', username, date, 'filename.ext')
    
    if not os.path.exists(file_path):
        return HttpResponseNotFound("File not found.")
    
    # Use FileResponse to stream the file to the user
    response = FileResponse(open(file_path, 'rb'))
    
    # Set content type based on the file extension
    if file_path.endswith('.pdf'):
        response['Content-Type'] = 'application/pdf'
    elif file_path.endswith('.png'):
        response['Content-Type'] = 'image/png'
    elif file_path.endswith('.jpg') or file_path.endswith('.jpeg'):
        response['Content-Type'] = 'image/jpeg'
    else:
        response['Content-Type'] = 'application/octet-stream'
        
    # Set Content-Disposition to force download
    response['Content-Disposition'] = 'attachment; filename="filename.ext"'
    
    return response
```

This code includes the following security measures:
- Check that only GET requests are accepted
- Validate username and date to prevent directory traversal attacks
- Set Content-Type header based on file extension to prevent content sniffing attacks
- Set Content-Disposition header to force download and prevent XSS attacks.