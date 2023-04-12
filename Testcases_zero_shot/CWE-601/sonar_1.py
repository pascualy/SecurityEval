def http_responser_redirect(request):
    '''
    get the target url from the request and redirect to it
    '''
    target_url = request.GET.get('url', None)
    if target_url:
        return HttpResponseRedirect(target_url)
    else:
        # handle error case where no target url is provided
        pass