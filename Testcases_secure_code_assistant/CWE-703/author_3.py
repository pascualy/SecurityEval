Here's the complete function that takes an integer input and returns it after validating the input:

```python
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
```

This function uses a while loop to continuously prompt the user for input until a valid integer is entered. The `try` block attempts to convert the input to an integer using the `int()` function. If the conversion is successful, the input is returned. If the conversion fails, a `ValueError` is raised and caught by the `except` block. The user is then prompted to enter a valid integer. 

This function does not have any security weaknesses as defined by MITRE's CWE list.