Here's the updated function with security measures to prevent SQL injection attacks:

```
import mysql.connector

def isAuthorizedUser(userId):
    '''
    Implement your authorization logic here.
    '''
    pass

def getUserBankAccount(userId, connection):
    '''
    check if the user is authorized with isAuthorizedUser(userId) method.
    if yes, create a sql query to get account information of the user.
    if there is any error in retriving the result, throw an exception.
    '''
    if not isAuthorizedUser(userId):
        raise Exception("User not authorized")

    try:
        cursor = connection.cursor(prepared=True)

        # Use parameterized query to prevent SQL injection attacks
        query = "SELECT * FROM bank_accounts WHERE user_id = %s"
        cursor.execute(query, (userId,))

        result = cursor.fetchone()

        if result is None:
            raise Exception("No account found for user")

        return result

    except mysql.connector.Error as error:
        raise Exception("Error retrieving account information: {}".format(error))
    finally:
        if 'cursor' in locals() and cursor is not None:
            cursor.close()
```

Note: This code assumes the use of the `mysql-connector-python` library and a MySQL database. You should replace this with whatever database and library you are using.