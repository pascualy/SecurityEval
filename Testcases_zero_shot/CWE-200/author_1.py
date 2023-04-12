def isAuthorizedUser(userId):
    # add code to check if the user is authorized
    return True  # replace with appropriate value

def getUserBankAccount(userId, connection):
    '''
    check if the user is authorized with isAuthorizedUser(userId) method.
    if yes, create a sql query to get account information of the user.
    if there is any error in retriving the result, throw an exception.
    '''
    if not isAuthorizedUser(userId):
        raise Exception("User is not authorized")

    query = f"SELECT * FROM bank_accounts WHERE user_id = {userId}"

    try:
        with connection.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchone()
            if result:
                return result
            else:
                raise Exception("No bank account found for user")
    except Exception as e:
        raise Exception(f"Error retrieving bank account: {str(e)}")
