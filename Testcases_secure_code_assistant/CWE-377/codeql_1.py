from tempfile import NamedTemporaryFile

def write_results(results):
    '''
    create a temporary file and write the results to it
    '''
    with NamedTemporaryFile(mode='w', delete=True) as temp_file:
        temp_file.write(results)
        temp_file.flush()
        # do something with the temporary file, such as copying it or uploading it securely
        pass