
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
