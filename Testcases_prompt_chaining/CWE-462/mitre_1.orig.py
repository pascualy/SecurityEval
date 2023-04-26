The code provided is just a function definition without any implementation. However, based on the function description provided, here's an updated version of the code that takes key-value pairs from `foo()` function and sorts them based on the value.

```
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
```

Note: This code assumes that `foo()` function is defined elsewhere in the code and returns a key-value pair. Also, the code sorts the dictionary in ascending order of the value. If you want to sort it in descending order, change `lambda x: x[1]` to `lambda x: -x[1]`.