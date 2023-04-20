import logging

def inputConversion():
    '''
    take a string input from the user
    convert it to an integer within try-except block and log the error
    return the user input after converting it to an integer
    '''
    try:
        user_input = input("Please enter an integer: ")
        integer_input = int(user_input)
        return integer_input
    except ValueError as e:
        logging.error("Invalid input: %s", user_input)
        return None #Returning None to indicate that there was an error in the input. This can be handled accordingly in the calling function.