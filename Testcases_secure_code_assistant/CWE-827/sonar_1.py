from lxml import etree

def getRoot(xml_file):
    '''
    create a XML parser and parse a XML file and return the root element
    '''
    try:
        with open(xml_file, 'r') as f:
            xml_data = f.read()
            root = etree.fromstring(xml_data)
            return root
    except IOError:
        print("Error: File not found or could not be opened.")
        return None
    except etree.XMLSyntaxError:
        print("Error: XML Syntax Error.")
        return None