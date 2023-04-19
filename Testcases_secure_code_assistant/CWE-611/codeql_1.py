@app.post("/upload")
def upload():
    '''
    get the xml_src from the request, parse it and return it as string
    '''
    xml_src = request.data
    try:
        parser = lxml.etree.XMLParser(resolve_entities=False, remove_comments=True)
        root = lxml.etree.fromstring(xml_src, parser)
        return lxml.etree.tostring(root, encoding='unicode')
    except Exception as e:
        return "Error: Invalid XML format"