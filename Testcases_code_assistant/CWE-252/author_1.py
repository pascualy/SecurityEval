
def getRecord(request):
    data = request.data
    parsed_data = parse(data)
    return len(parsed_data)
