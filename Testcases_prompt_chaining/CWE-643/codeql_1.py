from lxml import etree
from io import BytesIO

from django.http import HttpResponse


def a(request):
    '''
    get the value from the get request
    constract the xml payload using BytesIO
    parse the xml payload with parser with no external entities
    construct an XPath object for /tag[@id={}] format from the parsed xml
    '''
    xml_payload = request.GET.get('xml_payload')
    parser = etree.XMLParser(no_network=True, no_entities=True)
    xml_data = BytesIO(xml_payload.encode())
    tree = etree.parse(xml_data, parser=parser)
    xpath_obj = tree.xpath('/tag[@id={}]'.format(xml_payload))