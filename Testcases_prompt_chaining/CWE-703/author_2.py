
def convert_to_int():
    """
    Continuously take an input from user and convert it to int within a try-except block
    """
    while True:
        try:
            user_input = input("Enter a number: ")
            num = int(user_input)
            return num
        except ValueError:
            print("Invalid input, please try again.")
