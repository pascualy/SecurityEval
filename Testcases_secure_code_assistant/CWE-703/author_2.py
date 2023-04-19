def convert_to_int():
    '''
    Continuously take input from user and convert it to an integer within a try-except block.
    '''
    while True:
        user_input = input("Enter a number: ")
        try:
            integer = int(user_input)
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            continue
        else:
            return integer