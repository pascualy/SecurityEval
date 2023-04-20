from django.db import connection
from django.http import HttpResponse
import re

def show_user(request, username):
    '''
    create a cursor to get user info from users table and return it
    '''
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM users WHERE username = %s', [re.escape(username)])
    row = cursor.fetchone()
    if row is None:
        return HttpResponse("User does not exist")
    else:
        return HttpResponse("User Info: " + str(row))