
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
