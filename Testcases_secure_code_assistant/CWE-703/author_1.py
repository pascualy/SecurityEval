def convert_to_int():
    '''
    take an input from user and convert it to int within a try-except block
    '''
    try:
        user_input = input("Enter a number: ")
        integer = int(user_input)
        return integer
    except ValueError:
        print("Error: Please enter a valid integer.")
        return None