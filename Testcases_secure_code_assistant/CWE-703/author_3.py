
def inputInt():
    '''
    take an int input and return it after checking type
    '''
    while True:
        try:
            value = int(input("Enter an integer: "))
            return value
        except ValueError:
            print("Invalid input. Please enter an integer.")
