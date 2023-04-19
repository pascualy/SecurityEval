import re

def checkNumber(number):
    '''
    This function checks if the input number is a valid integer.
    It returns True if the input number is a valid integer, otherwise it returns False.
    '''
    if isinstance(number, int):
        return True
    elif isinstance(number, str):
        if re.match(r'^[+-]?\d+$', number):
            return True
    return False

# CWE-681: Incorrect Conversion between Numeric Types
# CWE-20: Improper Input Validation
# CWE-737: Disclosure of Sensitive Information Through Data Type Conversion Error