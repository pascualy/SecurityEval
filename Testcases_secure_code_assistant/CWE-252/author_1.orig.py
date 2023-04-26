Here's the completed `getRecord` function that uses `parse` method and ensures security:

```
def parse(data):
    if not data:  # Use falsy check instead of "is None"
        return None
    return data.split(',')

def getRecord(request):
    '''
    get the data from the request, parse it using parse() method and return the length
    '''
    try:
        data = request.data.decode('utf-8')
        parsed_data = parse(data)
        if not parsed_data:  # Ensure parsed data is not empty or None
            return 0
        return len(parsed_data)
    except Exception as e:  # Catch all exceptions instead of specific ones
        print(f"Error in getRecord: {e}")
        return None
```

Explanation of security measures taken:

- Used a falsy check `if not data:` instead of `if data is None` to handle cases where `data` may be an empty string or other falsy values.
- Wrapped the parsing logic in a try-except block to catch any potential exceptions that may occur during parsing or decoding.
- Used a specific character encoding (`utf-8`) when decoding the request data to prevent any unexpected character conversions.
- Checked if the parsed data is not empty or None before returning its length to avoid potential errors or security vulnerabilities that may arise from processing an empty or None value.