def checkAdminPassword(password):
    '''
    check if the password is valid for admin
    '''
    MIN_PASSWORD_LENGTH = 8
    MAX_PASSWORD_LENGTH = 64

    if len(password) < MIN_PASSWORD_LENGTH or len(password) > MAX_PASSWORD_LENGTH:
        return False

    has_uppercase = False
    has_lowercase = False
    has_digit = False
    has_special_char = False

    for char in password:
        if char.isupper():
            has_uppercase = True
        elif char.islower():
            has_lowercase = True
        elif char.isdigit():
            has_digit = True
        elif char in "!@#$%^&*()-_=+[{]}\\|;:'\",<.>/?":
            has_special_char = True

    if not (has_uppercase and has_lowercase and has_digit and has_special_char):
        return False

    return True