
from lxml import etree

def get_root(xml_file, xsd_file):
    '''
    create a XML parser, parse from a file, validate the XML and return the root element
    '''
    # create the XML parser and schema
    xml_parser = etree.XMLParser(dtd_validation=True)
    schema = etree.XMLSchema(etree.parse(xsd_file))

    # parse the XML file and validate against the schema
    try:
        tree = etree.parse(xml_file, xml_parser)
        schema.assertValid(tree)
    except etree.XMLSyntaxError as e:
        print("XML syntax error:", e)
    except etree.DocumentInvalid as e:
        print("XML validation error:", e)

    # return the root element
    root = tree.getroot()
    return root
