
def validate_password(actual_pw, typed_pw):
    '''
    Compare the actual password with the typed password by checking every character.

    Args:
        actual_pw (str): The actual password.
        typed_pw (str): The password typed by the user.

    Returns:
        bool: True if the passwords match, False otherwise.
    '''
    if len(actual_pw) != len(typed_pw):
        return False
    for i in range(len(actual_pw)):
        if actual_pw[i] != typed_pw[i]:
            return False
    return True
