To make this code more secure, we can add input validation to ensure that the input `n` is a positive integer. We can also add a try-except block to catch any potential errors that may occur during the execution of the function. Here's the updated code:

```
def getFibonacci(n):
    '''
    get n-th fibonacci number using loop
    '''
    try:
        n = int(n)
        if n <= 0:
            raise ValueError("Input must be a positive integer")
    except ValueError:
        print("Input must be a positive integer")
        return None
    
    # Initialize variables for first two Fibonacci numbers
    a, b = 0, 1
    
    # Loop to calculate nth Fibonacci number
    for i in range(n):
        a, b = b, a + b
    
    return a
```

This updated code validates the input to ensure that it's a positive integer. If the input is not valid, it returns None and prints an error message to the console. If the input is valid, it calculates the nth Fibonacci number using a loop and returns the result.