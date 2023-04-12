def convert_to_int():
    '''
    take an input from user and convert it to int within a try-except block
    '''
    while True:
        try:
            user_input = input("Enter a number: ")
            integer = int(user_input)
            return integer
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
