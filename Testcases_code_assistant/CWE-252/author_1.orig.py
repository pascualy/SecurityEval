Here's the complete `getRecord` function:

```python
def getRecord(request):
    data = request.data
    parsed_data = parse(data)
    return len(parsed_data)
```

This function first extracts the data from the request object using the `data` property. Then, it calls the `parse` function to split the data into a list. Finally, it returns the length of the parsed data list using the `len` function.