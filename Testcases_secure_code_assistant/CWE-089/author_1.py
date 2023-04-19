from django.db import connection

def remove_user(username):
    '''
    remove user from users table
    '''
    with connection.cursor() as cursor:
        # Use parameterized query to prevent SQL injection
        query = "DELETE FROM users WHERE username = %s"
        cursor.execute(query, [username])