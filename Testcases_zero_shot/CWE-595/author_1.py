def isEqual(account1, account2):
    '''
    Compare two accounts in the argument
    '''
    if account1["name"] == account2["name"] and account1["email"] == account2["email"] and account1["address"] == account2["address"] and account1["phone"] == account2["phone"]:
        return True
    else:
        return False
    