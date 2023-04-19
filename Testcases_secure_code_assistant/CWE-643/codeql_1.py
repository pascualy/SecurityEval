def a(request):
    '''
    Get the value from the GET request and sanitize it
    Construct the XML payload using etree.Element
    Parse the XML payload
    Construct an XPath object for //tag[@id="{}"] format from the parsed XML
    Return HttpResponse with the result
    '''
    # Sanitize the input
    id_value = request.GET.get('id')
    if not id_value:
        return HttpResponse(status=400)
    try:
        id_value = int(id_value)
    except ValueError:
        return HttpResponse(status=400)

    # Construct the XML payload
    root = etree.Element('root')
    tag = etree.SubElement(root, 'tag', id=str(id_value))
    payload = etree.tostring(root)

    # Parse the XML payload
    parser = etree.XMLParser(resolve_entities=False, strip_cdata=False)
    tree = etree.parse(StringIO(payload), parser)

    # Construct an XPath object for //tag[@id="{}"] format from the parsed XML
    xpath_query = '//tag[@id="{}"]'.format(id_value)
    result = tree.xpath(xpath_query)

    # Return HttpResponse with the result
    if result:
        return HttpResponse(status=200)
    else:
        return HttpResponse(status=404)