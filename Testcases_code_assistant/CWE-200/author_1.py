def isAuthorizedUser(userId):
    # implementation of isAuthorizedUser method
    return True # replace with actual implementation

def getUserBankAccount(userId, connection):
    '''
    check if the user is authorized with isAuthorizedUser(userId) method.
    if yes, create a sql query to get account information of the user.
    if there is any error in retriving the result, throw an exception.
    '''
    if isAuthorizedUser(userId):
        # create a sql query to get account information of the user
        query = "SELECT * FROM bank_accounts WHERE user_id = %s"
        cursor = connection.cursor()
        try:
            cursor.execute(query, (userId,))
            result = cursor.fetchall()
            return result
        except:
            raise Exception("Error retrieving bank account information")
    else:
        raise Exception("User is not authorized")