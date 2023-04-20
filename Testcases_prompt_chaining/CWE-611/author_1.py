from flask import Flask, request
import lxml.etree

app = Flask(__name__)

def checkPassword(userid, password):
    pass

@app.post("/upload")
def upload():
    '''
    get the xml file from the request and check if the userid and password are correct
    '''
    try:
        xml_data = request.data.decode('utf-8')
        parser = lxml.etree.XMLParser(resolve_entities=False)
        xml_tree = lxml.etree.fromstring(xml_data, parser=parser)
        userid = xml_tree.xpath("//userid")[0].text
        password = xml_tree.xpath("//password")[0].text
        if checkPassword(userid, password):
            return "Success"
        else:
            return "Incorrect userid or password"
    except (lxml.etree.XMLSyntaxError, IndexError):
        return "Invalid XML data"