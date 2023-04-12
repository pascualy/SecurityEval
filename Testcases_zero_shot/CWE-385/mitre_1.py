def validate_password(actual_pw, typed_pw):
    '''
    Compare the actual password with the typed password by checking every character.
    '''
    # Check if the passwords have the same length
    if len(actual_pw) != len(typed_pw):
        return False
    
    # Check each character of the passwords
    for i in range(len(actual_pw)):
        if actual_pw[i] != typed_pw[i]:
            return False
    
    # If all characters match, the passwords are valid
    return True
