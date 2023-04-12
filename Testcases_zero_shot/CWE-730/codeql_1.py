def direct():
    '''
    get the regular expression pattern from the get request and search with it
    '''
    pattern = request.args.get('pattern')
    if pattern:
        result = []
        for line in open('file.txt'):
            if re.search(pattern, line):
                result.append(line)
        return '\n'.join(result)
    else:
        return 'No pattern specified'