import logging

def inputConversion():
    '''
    take a string input from the user
    convert it to an integer within try-except block and log the error
    return the user input after converting it to an integer
    '''
    user_input = input("Enter an integer: ")
    try:
        user_input = int(user_input)
    except ValueError as e:
        logging.error("Error: %s", e)
        return None
    return user_input