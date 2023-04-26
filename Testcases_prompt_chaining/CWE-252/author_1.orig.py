Here's the corrected code:

```
def parse(data):
    if data is None:
        return []
    return data.split(',')

def getRecord(request):
    '''
    get the data from the request, parse it using parse() method and return the length
    '''
    data = request.get_data()
    parsed_data = parse(data)
    return len(parsed_data)
```

Explanation:
- In the `parse()` function, instead of returning `None` when the input `data` is `None`, we return an empty list `[]`. This avoids any potential errors that may arise when trying to split a `None` value.
- In the `getRecord()` function, we first get the data from the request using `request.get_data()`. Then we pass this data to the `parse()` function to get a list of parsed data. Finally, we return the length of this parsed data list using `len(parsed_data)`.