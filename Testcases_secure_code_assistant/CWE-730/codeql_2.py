@app.route("/direct")
def direct():
    '''
    get the regular expression pattern from the get request, compile it and then use it for search
    '''
    pattern = request.args.get('pattern')
    if not pattern:
        return "Error: Please provide a regular expression pattern."
    
    try:
        regex = re.compile(pattern)
    except re.error:
        return "Error: Invalid regular expression pattern."
    
    data = request.args.get('data')
    if not data:
        return "Error: Please provide data to search."
    
    match = regex.search(data)
    if not match:
        return "No matches found."
    
    return match.group()