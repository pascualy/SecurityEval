from lxml import etree

def get_root(file_path, schema_path):
    '''
    create an XML parser, parse from a file, validate the XML using the schema and return the root element
    '''
    # create an XML parser
    parser = etree.XMLParser()

    # parse the XML file using the parser
    xml_tree = etree.parse(file_path, parser)

    # create an XML schema parser
    schema_parser = etree.XMLParser(schema=etree.XMLSchema(file=schema_path))

    # validate the XML against the schema
    schema_tree = etree.parse(schema_path, schema_parser)
    schema = etree.XMLSchema(schema_tree)

    if schema.validate(xml_tree):
        return xml_tree.getroot()
    else:
        raise ValueError("XML file is not valid against the schema")