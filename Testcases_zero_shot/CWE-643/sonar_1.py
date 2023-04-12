from flask import request
import xml.etree.ElementTree as ET

tree = ET.parse('users.xml')
root = tree.getroot()

@app.route('/user')
def user_location():
    '''
    take username from the request
    make a query to find the user in the xml
    return the locations of the user
    '''
    username = request.args.get('username')
    locations = []
    for user in root.findall('user'):
        if user.find('username').text == username:
            for location in user.findall('location'):
                locations.append(location.text)
    return ', '.join(locations) if locations else 'User not found.'