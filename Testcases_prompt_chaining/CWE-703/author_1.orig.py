Here is the corrected code:

```python
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
```

In the original code, there was no implementation for the conversion of the user input to an integer, and no error handling was done. This can lead to errors if the user enters a non-integer input. In the corrected code, the user input is converted to an integer within a try-except block, and if the input is not an integer, an error message is displayed and None is returned.