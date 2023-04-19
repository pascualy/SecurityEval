from flask import Flask, request
import lxml.etree

app = Flask(__name__)

@app.post("/upload")
def upload():
    '''
    get the xml_src from the request, parse it and return it as string
    '''
    xml_file = request.files['xml_src']
    xml_string = xml_file.read()
    root = lxml.etree.fromstring(xml_string)
    return lxml.etree.tostring(root)