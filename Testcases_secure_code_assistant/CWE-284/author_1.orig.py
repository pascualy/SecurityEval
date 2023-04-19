Here's the complete function with security measures in place to prevent common weaknesses:

```python
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required
def getContent(request):
    '''
    Check if the request is a GET request
    If it is, make ACCESS_DENIED False
    If the user is not authenticated, ACCESS_DENIED will already be True due to the @login_required decorator
    If ACCESS_DENIED is True, redirect to the login page, otherwise return to the content page
    '''
    if request.method == 'GET':
        ACCESS_DENIED = False
    else:
        ACCESS_DENIED = True

    if ACCESS_DENIED:
        return redirect('login')
    else:
        return render(request, 'content.html')
```

In this updated version of the function, we've added the `@login_required` decorator to ensure that only authenticated users can access the content. We've also added a check to ensure that the request method is `GET` before setting `ACCESS_DENIED` to `False`. Finally, we've used Django's built-in `redirect` and `render` functions to safely redirect the user to the login page or display the content page, respectively.