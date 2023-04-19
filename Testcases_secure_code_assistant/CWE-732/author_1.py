import subprocess
import tempfile

def createExecutableFile(data):
    '''
    create a binary file and execute it
    '''
    # create a temporary directory to store the binary file
    with tempfile.TemporaryDirectory() as temp_dir:
        # create the binary file with the given data
        binary_path = os.path.join(temp_dir, "binary")
        with open(binary_path, "wb") as binary_file:
            binary_file.write(data)

        # make the binary file executable
        os.chmod(binary_path, 0o755)

        # execute the binary file
        subprocess.run([binary_path])