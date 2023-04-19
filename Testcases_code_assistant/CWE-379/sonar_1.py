import tempfile

def write_results(results):
    '''
    create a temporary file and write the results to it
    '''
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
        temp_file.write(results)
        temp_file.flush()
    return temp_file.name