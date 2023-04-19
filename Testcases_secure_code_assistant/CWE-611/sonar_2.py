from lxml import etree

def get_root(xml_file_path, xsd_file_path):
    '''
    create an XML parser, parse from a file, validate the XML and return the root element
    '''
    try:
        # create an XML parser
        parser = etree.XMLParser()

        # parse the XML file
        xml_tree = etree.parse(xml_file_path, parser)

        # create a schema parser
        schema_parser = etree.XMLParser()
  
        # parse the XSD file
        xsd_tree = etree.parse(xsd_file_path, schema_parser)

        # create a schema object
        schema = etree.XMLSchema(xsd_tree)

        # validate the XML against the schema
        schema.assertValid(xml_tree)

        # get the root element
        root = xml_tree.getroot()

        return root

    except etree.XMLSyntaxError as e:
        print("Error parsing XML:", e)
    except etree.DocumentInvalid as e:
        print("Error validating XML:", e)