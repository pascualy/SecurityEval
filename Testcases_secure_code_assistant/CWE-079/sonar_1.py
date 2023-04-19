from flask import request, make_response
import os

@xss.route('/insecure/no_template_engine_replace', methods =['GET'])
def no_template_engine_replace():
    '''
    get the param data from request
    open html file and replace the name with the param data
    return the html file as reponse
    '''

    # Get the parameter data from request
    name = request.args.get('name', default='')

    # Check if name is empty
    if not name:
        return make_response('Name parameter is missing', 400)

    # Read the html file
    with open(os.path.join(os.path.dirname(__file__), 'template.html'), 'r') as file:
        html = file.read()

    # Replace the name in the html file
    html = html.replace('{{name}}', name)

    # Return the html file as response
    response = make_response(html)
    response.headers['Content-Type'] = 'text/html'
    return response