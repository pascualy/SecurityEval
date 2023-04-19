import xml.sax

class MyHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.current_element = ""
        self.root = None

    def startElement(self, name, attrs):
        self.current_element = name
        if self.root is None:
            self.root = name

    def characters(self, content):
        pass

    def endElement(self, name):
        pass

def get_root():
    '''
    create a XML parser, handler, feature
    parse from a file and return the result
    '''
    try:
        parser = xml.sax.make_parser()
        parser.setFeature(xml.sax.handler.feature_namespaces, 0)

        handler = MyHandler()
        parser.setContentHandler(handler)

        with open("file.xml", "r") as f:
            parser.parse(f)

        return handler.root
    except Exception as e:
        print("Error: ", e)
        return None

# Ensure that the file is being run directly and not imported
if __name__ == '__main__':
    get_root()