from lxml import etree

def get_root(file_path):
    '''
    create a XML parser, parse from a file and return the root
    '''
    parser = etree.XMLParser()
    with open(file_path, 'rb') as f:
        tree = etree.parse(f, parser=parser)
    root = tree.getroot()
    return root

# CWE-22: Improper Limitation of a Pathname to a Restricted Directory ('Path Traversal')
# Ensure that the file_path argument is a valid path to a file within the desired directory and not a path to a different directory.