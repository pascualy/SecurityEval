def show_user(request, username):
    '''
    create a cursor to get user info from users table and return it
    '''
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM users WHERE username = %s", [username])
        user = cursor.fetchone()
    return user