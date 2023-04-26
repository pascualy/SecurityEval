
def isEqual(account1, account2):
    '''
    compare two accounts in the argument
    '''
    if account1.account_number == account2.account_number and \
        account1.balance == account2.balance and \
        account1.account_holder == account2.account_holder:
        return True
    else:
        return False
