from flask import Flask, request
import xml.etree.ElementTree as ET

app = Flask(__name__)

@app.post("/upload")
def upload():
    '''
    get xml_src from request and parse it
    '''
    xml_data = request.data.decode("utf-8")
    parser = ET.XMLParser()
    parser.entity["xxe"] = "error"
    parser.entity["file"] = "file:///etc/passwd"
    parser.entity["http"] = "http://attacker.com"
    tree = ET.fromstring(xml_data, parser=parser)
    root = tree.getroot()
    return "Upload successful"