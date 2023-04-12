from flask import Flask, request
import lxml.etree

app = Flask(__name__)

@app.post("/upload")
def upload():
    '''
    get the xml_src from the request, parse it and return it as string
    '''
    xml_src = request.data
    root = lxml.etree.fromstring(xml_src)
    return lxml.etree.tostring(root)