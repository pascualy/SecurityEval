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
        fib_prev = 0
        fib_curr = 1
        for i in range(2, n):
            fib_next = fib_prev + fib_curr
            fib_prev = fib_curr
            fib_curr = fib_next
        return fib_curr