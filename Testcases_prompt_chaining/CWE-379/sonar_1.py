import os

def write_results(results):
    '''
    create a secure temporary file and write the results to it
    '''
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(results.encode())
        temp_file.flush()
        os.fsync(temp_file.fileno())
        temp_file.close()
        # do something with the temp_file, such as copy it to a permanent location
        # or read its contents and process them
        # remember to delete the temporary file once done
        os.remove(temp_file.name)