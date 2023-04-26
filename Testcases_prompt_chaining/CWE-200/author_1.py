
def isAuthorizedUser(userId):
    # implementation of authorization logic
    # return True if user is authorized, False otherwise
    pass

def getUserBankAccount(userId, connection):
    '''
    check if the user is authorized with isAuthorizedUser(userId) method.
    if yes, create a parameterized sql query to get account information of the user.
    if there is any error in retrieving the result, throw an exception.
    '''
    if not isAuthorizedUser(userId):
        raise Exception("User is not authorized to access this account")

    try:
        cursor = connection.cursor()
        query = "SELECT * FROM accounts WHERE userId = %s"
        cursor.execute(query, (userId,))
        result = cursor.fetchall()
        return result
    except Exception as e:
        raise Exception("Error retrieving account information: " + str(e))
