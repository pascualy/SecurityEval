
def convert_to_int():
    '''
    take an input from user and convert it to int within a try-except block
    '''
    user_input = input("Enter an integer: ")
    try:
        int_input = int(user_input)
        return int_input
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return None
