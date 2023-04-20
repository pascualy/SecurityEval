from lxml import etree

def get_root(xml_file):
    '''
    create a XML parser and parse a XML file and return the root element
    '''
    try:
        tree = etree.parse(xml_file)
        root = tree.getroot()
        return root
    except etree.XMLSyntaxError:
        print("Error: Invalid XML syntax in file: ", xml_file)
        return None