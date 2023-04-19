import xml.etree.ElementTree as ET

def parse_xml(xml_string):
    '''
    parse xml_string and return the root element
    '''
    try:
        root = ET.fromstring(xml_string)
    except ET.ParseError:
        raise ValueError('Invalid XML string')
    return root