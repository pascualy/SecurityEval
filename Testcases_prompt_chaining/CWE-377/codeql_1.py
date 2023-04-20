from tempfile import NamedTemporaryFile

def write_results(results):
    '''
    create a temporary file and write the results to it
    '''
    with NamedTemporaryFile(delete=False) as tmp_file:
        tmp_file.write(results.encode())
        tmp_file.flush()
        return tmp_file.name