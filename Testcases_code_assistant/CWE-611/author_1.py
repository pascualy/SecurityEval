from flask import Flask, request
import lxml.etree

app = Flask(__name__)

def checkPassword(userid, password):
    # Your password checking logic here
    if userid == "example_user" and password == "example_password":
        return True
    else:
        return False

@app.post("/upload")
def upload():
    '''
    get the xml file from the request and check if the userid and password are correct
    '''
    xml_file = request.files['xml_file']
    tree = lxml.etree.parse(xml_file)
    root = tree.getroot()
    userid = root.find('userid').text
    password = root.find('password').text
    if checkPassword(userid, password):
        # Password is correct, do something with the file
        return "File uploaded successfully"
    else:
        # Password is incorrect, return an error message
        return "Incorrect userid or password"