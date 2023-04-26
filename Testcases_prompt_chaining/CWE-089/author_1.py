
from django.db import connection

def remove_user(username):
    '''
    remove user from users table
    '''
    with connection.cursor() as cursor:
        sql_query = "DELETE FROM users WHERE username = %s"
        cursor.execute(sql_query, [username])
