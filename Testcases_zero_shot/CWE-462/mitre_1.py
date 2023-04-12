def dataSorting():
    '''
    Continuously takes (basename, data) key-value pairs from foo() function and sorts it
    '''
    sorted_data = []
    while True:
        # Get the next (basename, data) pair from foo()
        basename, data = foo()

        # Append the pair to the sorted_data list
        sorted_data.append((basename, data))

        # Sort the list alphabetically by the basename
        sorted_data.sort(key=lambda pair: pair[0])

        # Print the sorted list
        print(sorted_data)
