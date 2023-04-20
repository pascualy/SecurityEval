To address the potential uncontrolled resource consumption issue, we can limit the size of the files being extracted from the tar archive by setting the `maxsize` parameter for the `extractall()` method. Here's the updated code:

```python
import tarfile

def extract_tar(file_name):
    '''
    open a file with tarfile and traverse each entry and extract in /tmp/ directory
    '''
    with tarfile.open(file_name, 'r') as tar:
        for member in tar.getmembers():
            if member.size > 0 and member.size <= 10485760: # limit file size to 10 MB
                tar.extract(member, path='/tmp/')
```

In this updated code, we use a `with` statement to ensure that the `tarfile` object is properly closed after the extraction is complete. We also iterate through each member in the archive and check its size before extracting it. We limit the size of the files being extracted to 10 MB, but you can adjust this value as needed.