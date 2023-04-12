from tempfile import mktemp

def write_results(results):
    '''
    create a temporary file and write the results to it
    '''
    temp_file = mktemp()
    with open(temp_file, 'w') as file:
        file.write(results)