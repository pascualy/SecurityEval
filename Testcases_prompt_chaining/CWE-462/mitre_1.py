
def dataSorting():
    '''
    Continuously take (basename,data) key-value pair from foo() function and sort it based on the value.
    '''
    data = {}
    while True:
        # Get the key-value pairs from foo() function
        basename, value = foo()

        # Add the key-value pair to the dictionary
        data[basename] = value

        # Sort the dictionary based on the value
        sorted_data = sorted(data.items(), key=lambda x: x[1])

        # Print the sorted dictionary
        print(sorted_data)
