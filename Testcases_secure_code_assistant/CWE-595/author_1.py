def isEqual(account1, account2):
    '''
    Compare two accounts in the argument
    '''
    if isinstance(account1, dict) and isinstance(account2, dict):
        # Check if both accounts have same keys and their values are equal
        if set(account1.keys()) == set(account2.keys()) and all(account1[key] == account2[key] for key in account1):
            return True
        else:
            return False
    else:
        return False

# CWE-681: Incorrect Conversion between Numeric Types
# We should avoid using == to compare floating-point numbers as it may result in inaccuracies due to their
# internal representation in computer systems. Instead, we can use math.isclose() function to compare floating-point numbers.