Here is the complete function:

```python
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
```

This function takes two arguments: `xml_file` and `xsd_file`, which are the paths to the XML file and its corresponding XSD schema file, respectively. It first creates an XML parser and a schema object, then parses the XML file with validation against the schema. If there are any errors, it prints a message and returns `None`. Otherwise, it returns the root element of the XML tree.