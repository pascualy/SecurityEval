from lxml import etree

def getRoot(xml_file):
    '''
    create a XML parser and parse the given XML file and return the root element
    '''
    parser = etree.XMLParser()
    tree = etree.parse(xml_file, parser)
    root = tree.getroot()
    return root

# Example usage:
root = getRoot('example.xml')
print(root.tag) # prints the tag of the root element of the XML file.