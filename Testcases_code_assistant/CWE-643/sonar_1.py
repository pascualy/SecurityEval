
from flask import request
import xml.etree.ElementTree as ET

# assuming this code is inside a Flask app

@app.route('/user')
def user_location():
    '''
    take username from the request
    make a query to find the user in the xml
    return the locations of the user
    '''
    username = request.args.get('username')
    if username is None:
        return 'Please provide a username in the request parameters.', 400

    tree = ET.parse('users.xml')
    root = tree.getroot()

    user = root.find(f"./user[@name='{username}']")
    if user is None:
        return f"No user found with username '{username}'.", 404

    locations = user.findall('./location')
    if len(locations) == 0:
        return f"No locations found for user '{username}'.", 404

    response = {
        'username': username,
        'locations': [location.text for location in locations]
    }

    return response, 200
