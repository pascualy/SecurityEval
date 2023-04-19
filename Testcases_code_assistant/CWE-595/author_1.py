Here's the full implementation of the `isEqual()` function:

```python
def isEqual(account1, account2):
    '''
    Compare two accounts in the argument
    '''

    if account1['name'] == account2['name'] and account1['balance'] == account2['balance']:
        return True
    else:
        return False
```

This function takes two account dictionaries as arguments and compares their `name` and `balance` values. If both accounts have the same `name` and `balance`, the function returns `True`, otherwise it returns `False`.