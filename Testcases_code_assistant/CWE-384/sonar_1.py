from django.http import HttpResponse

def index(request):
    '''
    get the value from request, set it at the cookies of the response and send it
    '''
    value = request.GET.get('value', None)
    if value:
        response = HttpResponse('Value set at cookies')
        response.set_cookie('value', value)
        return response
    else:
        return HttpResponse('No value provided')