import xml.sax

def get_root(file_path):
    '''
    create a XML parser, handler, feature
    parse from a file and return the result
    '''
    class MyHandler(xml.sax.ContentHandler):
        def startElement(self, name, attrs):
            pass
        
    parser = xml.sax.make_parser()
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)
    handler = MyHandler()
    parser.setContentHandler(handler)
    parser.parse(file_path)
    
    return handler.getDocumentLocator().getSystemId()