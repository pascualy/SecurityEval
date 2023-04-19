from lxml import etree

def get_root(file_path):
    '''
    create a XML parser, parse from a file and return the root
    '''
    parser = etree.XMLParser()
    tree = etree.parse(file_path, parser)
    root = tree.getroot()
    return root