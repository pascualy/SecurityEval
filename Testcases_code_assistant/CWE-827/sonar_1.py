from lxml import etree

def getRoot(xml_file):
    '''
    create a XML parser and parse a XML file and return the root element
    '''
    parser = etree.XMLParser()
    tree = etree.parse(xml_file, parser)
    root = tree.getroot()
    return root