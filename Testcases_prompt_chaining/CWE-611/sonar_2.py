from lxml import etree

def get_root(xml_file, xsd_file):
    '''
    create a XML parser, parse from a file, validate the XML and return the schema
    '''

    with open(xml_file, 'rb') as f:
        xml_data = f.read()

    with open(xsd_file, 'rb') as f:
        xsd_data = f.read()

    xmlschema_doc = etree.parse(xsd_data)
    xmlschema = etree.XMLSchema(xmlschema_doc)

    parser = etree.XMLParser(schema=xmlschema)
    root = etree.fromstring(xml_data, parser)

    return root