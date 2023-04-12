import xml.sax

def get_root(file_path):
    '''
    create a XML parser, handler, feature
    parse from a file and return the result
    '''
    class MyHandler(xml.sax.ContentHandler):
        def __init__(self):
            self.root = None

        def startElement(self, name, attrs):
            if self.root is None:
                self.root = name

    parser = xml.sax.make_parser()
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)
    handler = MyHandler()
    parser.setContentHandler(handler)
    parser.parse(file_path)
    return handler.root