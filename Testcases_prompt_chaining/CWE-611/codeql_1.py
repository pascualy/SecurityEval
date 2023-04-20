from flask import Flask, request
import lxml.etree

app = Flask(__name__)

@app.route("/upload", methods=['POST'])
def upload():
    '''
    get the xml_src from the request, parse it and return it as string
    '''
    try:
        xml_src = request.data.decode('utf-8')
        parser = lxml.etree.XMLParser(resolve_entities=False, strip_cdata=False)
        root = lxml.etree.fromstring(xml_src, parser=parser)
        return lxml.etree.tostring(root, encoding='unicode')
    except Exception as e:
        return str(e), 400