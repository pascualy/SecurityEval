
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
