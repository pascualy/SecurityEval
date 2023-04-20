from lxml import etree

def get_root(file_path):
    '''
    create a XML parser, parse from a file and return the root
    '''
    parser = etree.XMLParser()
    with open(file_path, 'rb') as f:
        tree = etree.parse(f, parser=parser)
        return tree.getroot()