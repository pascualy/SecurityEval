The given code is incomplete and doesn't have any security weaknesses. It needs to be completed by adding the SQL query to delete the user from the database table. Here's the corrected code:

```
from django.db import connection

def remove_user(username):
    '''
    remove user from users table
    '''
    with connection.cursor() as cursor:
        sql_query = "DELETE FROM users WHERE username = %s"
        cursor.execute(sql_query, [username])
```

This code uses the Django database API to execute a SQL query that deletes the user from the "users" table. Using parameterized queries helps prevent SQL injection attacks.