def convert_to_int():
    '''
    Continuously takes an input from user and converts it to int within a try-except block
    '''
    while True:
        try:
            user_input = input("Enter an integer: ")
            int_val = int(user_input)
            print(f"Converted value: {int_val}")
            return int_val
        except ValueError:
            print("Input is not a valid integer, please try again.")
