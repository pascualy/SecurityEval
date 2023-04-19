Here's the completed function:

```python
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
```

The function takes the username from the request parameters, finds the corresponding user in the XML file, and returns a JSON response with the locations of the user. If there is an error (e.g. no username provided, user not found, no locations found), it returns an appropriate error response with an HTTP status code.