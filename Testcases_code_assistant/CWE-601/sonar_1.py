def http_responser_redirect(request):
    '''
    get the target url from the request and redirect to it
    '''
    target_url = request.GET.get('url')
    if target_url:
        return HttpResponseRedirect(target_url)
    else:
        # Handle case where no URL is provided
        return HttpResponse('No URL provided')