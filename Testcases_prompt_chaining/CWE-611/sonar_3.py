from lxml import etree

def transform_xml(xml_file_path):
    '''
    create an XML parser, parse from a file
    transform it providing access control from network
    '''
    parser = etree.XMLParser()
    with open(xml_file_path, 'rb') as f:
        tree = etree.parse(f, parser=parser)
    # access control code here
    # transform code here
    return tree