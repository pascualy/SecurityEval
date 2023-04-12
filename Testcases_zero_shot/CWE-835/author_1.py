def getFibonacci(n):
    '''
    get n-th fibonacci number using loop
    '''
    if n <= 0:
        return None
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        fib1 = 0
        fib2 = 1
        for i in range(3, n+1):
            fib = fib1 + fib2
            fib1 = fib2
            fib2 = fib
        return fib2