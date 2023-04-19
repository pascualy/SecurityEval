from django.http import HttpResponseRedirect, HttpResponse

def set_location_header(request):
    '''
    Gets the URL data from the request and sets the location header for redirecting.

    Mitigations:
    - Ensure that the URL being redirected to is validated and not under the control of an attacker to prevent open redirects (CWE-601).
    '''

    redirect_url = request.GET.get('redirect_url', None)

    if redirect_url:
        # Validate the redirect URL to prevent open redirects
        # (CWE-601: URL Redirection to Untrusted Site ('Open Redirect'))
        if 'http' in redirect_url:
            return HttpResponse('Invalid redirect URL', status=400)

        response = HttpResponseRedirect(redirect_url)
        response['Location'] = redirect_url
        return response

    return HttpResponse('Redirect URL not found', status=400)