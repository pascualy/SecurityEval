import re
def checkNumber(number):
    '''
    use regular expression to match lines with numbers
    '''
    pattern = r'\d+' # regular expression pattern to match one or more digits
    if re.match(pattern, number):
        return True
    else:
        return False