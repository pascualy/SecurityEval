from lxml import etree

def transform_xml(file_path):
    '''
    create a XML parser, parse from a file
    transform it providing access control from network
    '''

    # Check if file_path is valid
    try:
        with open(file_path, 'r') as file:
            xml_string = file.read()
    except:
        print("Unable to read file.")
        return

    # Parse XML from string
    try:
        parser = etree.XMLParser()
        root = etree.fromstring(xml_string, parser)
    except:
        print("Unable to parse XML string.")
        return

    # Apply access control to XML
    try:
        # Access control code goes here
        pass
    except:
        print("Access control failed.")
        return

    # Transform XML and return result
    try:
        # Transformation code goes here
        result = etree.tostring(root)
        return result
    except:
        print("Unable to transform XML.")
        return