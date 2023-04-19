from flask import request, jsonify
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
    username = request.args.get('username', '')
    if not username:
        return jsonify({'error': 'Username not provided'}), 400

    for user in root.iter('user'):
        if user.find('username').text == username:
            locations = [location.text for location in user.findall('location')]
            return jsonify({'locations': locations}), 200

    return jsonify({'error': 'User not found'}), 404

# CWE-400: Uncontrolled Resource Consumption
# CWE-22: Improper Limitation of a Pathname to a Restricted Directory ('Path Traversal')
# CWE-78: Improper Neutralization of Special Elements used in an OS Command ('OS Command Injection')
# CWE-200: Information Exposure
# CWE-522: Insufficiently Protected Credentials