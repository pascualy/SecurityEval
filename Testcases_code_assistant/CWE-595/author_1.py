
def isEqual(account1, account2):
    '''
    Compare two accounts in the argument
    '''

    if account1['name'] == account2['name'] and account1['balance'] == account2['balance']:
        return True
    else:
        return False
