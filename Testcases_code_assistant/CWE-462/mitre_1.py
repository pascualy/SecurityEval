def dataSorting():
    '''
    Continuously take (basename,data) key-value pairs from foo() function and sort them.
    '''
    def foo():
        '''
        A generator function that yields (basename, data) key-value pairs.
        '''
        # Implement the generator function here.

    sorted_data = sorted(foo(), key=lambda x: x[0])
    # Return the sorted data.
    return sorted_data