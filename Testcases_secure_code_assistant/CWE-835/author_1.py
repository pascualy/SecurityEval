
def getFibonacci(n):
    '''
    get n-th fibonacci number using loop
    '''
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        prev = 0
        curr = 1
        for i in range(2, n+1):
            next_num = prev + curr
            prev = curr
            curr = next_num
        return curr
