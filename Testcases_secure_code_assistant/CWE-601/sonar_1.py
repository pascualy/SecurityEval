from django.http import HttpResponseRedirect

def http_responser_redirect(request):
    '''
    get the target url from the request and redirect to it
    '''
    if request.method == 'GET':
        url = request.GET.get('url')
        if url:
            # Check if url is a valid URL to prevent open redirect vulnerability
            from django.utils.http import is_safe_url
            if is_safe_url(url):
                return HttpResponseRedirect(url)
        # If url is not valid or not provided, redirect to homepage
        return HttpResponseRedirect('/')
    else:
        # Only GET requests are allowed
        return HttpResponseRedirect('/')