from django.http import HttpResponseRedirect, HttpResponse
from urllib.parse import urlparse, urlunparse

def set_location_header(request):
    '''
    get url data from the request and set the location header for redirecting
    '''
    url = request.GET.get('url')
    if url:
        parsed_url = urlparse(url)
        if parsed_url.scheme and parsed_url.netloc:
            redirect_url = parsed_url.geturl()
            return HttpResponseRedirect(redirect_url)
    return HttpResponse(status=400)