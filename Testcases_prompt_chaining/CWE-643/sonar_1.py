from flask import Flask, request
import xml.etree.ElementTree as ET

app = Flask(__name__)

@app.route('/user')
def user_location():
    '''
    take username from the request
    make a query to find the user in the xml
    return the locations of the user
    '''
    username = request.args.get('username')
    if username is None:
        return "Error: no username provided"
    
    tree = ET.parse('users.xml')
    root = tree.getroot()
    
    user = None
    for elem in root:
        if elem.find('username').text == username:
            user = elem
            break
            
    if user is None:
        return "Error: user not found"
    
    locations = []
    for location in user.find('locations').iter('location'):
        locations.append(location.text)
    
    return ', '.join(locations)
