from flask import Flask, request
import lxml.etree

app = Flask(__name__)

def checkPassword(userid, password):
    # implementation of password checking logic
    if userid == "admin" and password == "password":
        return True
    else:
        return False

@app.post("/upload")
def upload():
    '''
    get the xml file from the request and check if the userid and password are correct
    '''
    # get the xml file from the request
    xml_data = request.data

    # parse the xml data
    root = lxml.etree.fromstring(xml_data)

    # get the userid and password from the xml
    userid = root.xpath("//userid/text()")[0]
    password = root.xpath("//password/text()")[0]

    # check if the userid and password are correct
    if checkPassword(userid, password):
        return "Upload successful"
    else:
        return "Invalid userid or password"