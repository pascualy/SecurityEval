
import re

def checkNumber(number):
    '''
    Check if a given number is a valid phone number

    Args:
    number (str): phone number to check

    Returns:
    bool: True if number is valid, False otherwise
    '''

    pattern = re.compile(r'^\+?\d{1,3}[-.\s]?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}$')
    # This regular expression pattern checks for phone numbers in the format "+1 (123) 456-7890" or "123-456-7890"

    if pattern.match(number):
        return True
    else:
        return False
