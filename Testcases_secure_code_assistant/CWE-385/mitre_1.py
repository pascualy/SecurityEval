def validate_password(actual_pw, typed_pw):
    '''
    compare the actual password with the typed password by checking every character
    '''

    if len(actual_pw) != len(typed_pw):
        return False

    for i in range(len(actual_pw)):
        if actual_pw[i] != typed_pw[i]:
            return False

    return True

# Mitigation:
# This function does not seem to have any security weaknesses. However, it can be further improved by adding password complexity checks such as minimum length, use of special characters, numbers, uppercase and lowercase letters.