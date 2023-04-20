The given code is incomplete as it does not perform any comparison of the two accounts. You can add a simple comparison of account attributes to check if they are equal. Here is an example implementation:

```
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
```
This implementation assumes that the account objects have attributes `account_number`, `balance`, and `account_holder`, which are used for comparison. You can modify this implementation based on the actual attributes of the account objects.