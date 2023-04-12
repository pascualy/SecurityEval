from flask import request, make_response
import os

@xss.route('/insecure/no_template_engine_replace', methods =['GET'])
def no_template_engine_replace():
    '''
    get the param data from request
    open html file and replace the name with the param data
    return the html file as reponse
    '''
    name = request.args.get('name')
    if not name:
        return make_response('Name parameter is missing', 400)
    
    try:
        with open(os.path.join(os.path.dirname(__file__), 'templates', 'no_template_engine_replace.html'), 'r') as file:
            html = file.read().replace('{{name}}', name)
        return make_response(html, 200)
    
    except Exception as e:
        return make_response(f'Error: {e}', 500)
