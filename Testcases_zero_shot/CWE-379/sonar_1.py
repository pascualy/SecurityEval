import tempfile

def write_results(results):
    '''
    create a temporary file and write the results to it
    '''
    with tempfile.TemporaryFile(mode='w+') as f:
        f.write(results)
        f.seek(0)
        print(f.read())