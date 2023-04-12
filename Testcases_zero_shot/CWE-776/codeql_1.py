from flask import Flask, request
import xml.etree.ElementTree as ET

app = Flask(__name__)

@app.post("/upload")
def upload():
    '''
    get xml_src from request and parse it
    '''
    xml_src = request.data
    root = ET.fromstring(xml_src)
    
    # do something with the parsed XML
    
    return "XML uploaded successfully"