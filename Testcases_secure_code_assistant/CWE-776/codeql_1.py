@app.post("/upload")
def upload():
    '''
    get xml_src from request and parse it
    '''
    try:
        if not request.data:
            return "No data received", 400
        xml_src = request.data.decode('utf-8')
        if not xml_src:
            return "Empty request body", 400

        # parse the xml
        root = ET.fromstring(xml_src)
        # do something with the xml data
        # ...

        return "XML data successfully processed", 200
    except ET.ParseError:
        return "Invalid XML data", 400