import xml.etree.ElementTree as ET

def parse_xml(xml_string):
    '''
    parse xml_string and return the root element
    '''
    parser = ET.XMLParser()
    parser.entity["xxe"] = "no"
    return ET.fromstring(xml_string, parser=parser)