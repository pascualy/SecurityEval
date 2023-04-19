def direct():
    '''
    get the regular expression pattern from the get request and search with it
    '''
    pattern = request.args.get('pattern')
    text = request.args.get('text')
    result = re.findall(pattern, text)
    return ','.join(result)