import tempfile

def write_results(results):
    '''
    create a temporary file and write the results to it
    '''
    try:
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write(results)
            temp_file.flush()
            return True
    except Exception as e:
        print("Error occurred while writing to temporary file: ", str(e))
        return False