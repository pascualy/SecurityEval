def direct():
    pattern = request.args.get('pattern')  # get the regular expression pattern from the GET request
    if not pattern:  # check if pattern is None or empty
        return "Error: Please provide a pattern parameter in the request"
    
    try:
        compiled_pattern = re.compile(pattern)  # compile the pattern
    except re.error:
        return "Error: Invalid regular expression pattern"
    
    # search for the pattern in the request URL
    match = compiled_pattern.search(request.url)
    
    if match:
        return "Match found: {}".format(match.group())
    else:
        return "No match found for pattern: {}".format(pattern)