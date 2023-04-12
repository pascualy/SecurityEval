from lxml import etree
from io import BytesIO

def transform_xml(xml_file_path, schema_file_path, allowed_networks):
    '''
    create a XML parser, parse from a file
    transform it providing access control from network
    '''
    with open(xml_file_path, 'rb') as xml_file:
        xml_data = xml_file.read()
        
    with open(schema_file_path, 'rb') as schema_file:
        schema_data = schema_file.read()

    schema_doc = etree.parse(BytesIO(schema_data))
    xml_doc = etree.parse(BytesIO(xml_data))
    
    xmlschema = etree.XMLSchema(schema_doc)
    xmlschema.assertValid(xml_doc)

    #apply access control rules here based on allowed_networks
    
    transformed_xml = #apply transformation logic here
    
    return transformed_xml