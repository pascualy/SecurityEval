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
    
    # Perform further operations on the XML data here
    
    return "XML data successfully parsed"