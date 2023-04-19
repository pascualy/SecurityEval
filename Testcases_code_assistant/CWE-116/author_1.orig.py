Here's the complete function for you:

```python
def sendReply(request):
    '''
    read the data from request and send back the data as response as a HTML page
    '''
    if request.method == 'POST':
        data = request.POST.get('data')
        response = f'<html><body><h1>{data}</h1></body></html>'
        return HttpResponse(response)
    else:
        return HttpResponseBadRequest('Invalid Request')
```

This function checks if the request method is `POST`. If it is, it gets the `data` parameter from the POST request, creates an HTML response using that data, and returns it. If the request method is not `POST`, it returns an error response. Note that you'll need to import the `HttpResponse` and `HttpResponseBadRequest` classes.