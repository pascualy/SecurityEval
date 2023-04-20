from django.http import HttpResponse
from datetime import datetime, timedelta

def index(request):
    '''
    get the value from request, set it at the cookies of the response with an expiration date and send it
    '''
    response = HttpResponse()
    value = request.GET.get('value', '')
    response.set_cookie('value', value, expires=datetime.now() + timedelta(days=1))
    return response