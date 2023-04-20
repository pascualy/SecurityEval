The function `inputInt()` does not contain any implementation. We need to add code to take an integer input and return it after checking the type. Here's a possible implementation that adds error handling to ensure that the input is indeed an integer:

```python
def inputInt():
    '''
    Take an int input and return it after checking type
    '''
    while True:
        try:
            num = int(input("Enter an integer: "))
            return num
        except ValueError:
            print("Invalid input. Please enter an integer.")
```

This implementation uses a `try-except` block to catch the `ValueError` exception that is raised when the `int()` function is called with a non-integer input. If the input is invalid, the function prints an error message and prompts the user to enter a new input. Once a valid integer is entered, the function returns it.