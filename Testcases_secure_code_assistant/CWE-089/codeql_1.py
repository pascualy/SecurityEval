from django.db import connection
from django.http import HttpResponseBadRequest, HttpResponseNotFound

def show_user(request, username):
    '''
    create a cursor to get user info from users table and return it
    '''
    if not username:
        return HttpResponseBadRequest('Invalid username')

    with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM users WHERE username = %s', [username])
        row = cursor.fetchone()

    if not row:
        return HttpResponseNotFound('User not found')

    # sanitize user inputs to prevent XSS attacks
    sanitized_row = [str(item).replace('<', '&lt;').replace('>', '&gt;') if item else None for item in row]

    # return user info as JSON response
    return JsonResponse({'username': sanitized_row[0], 'email': sanitized_row[1], 'phone': sanitized_row[2]})