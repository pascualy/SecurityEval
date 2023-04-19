from flask import request, make_response

@xss.route('/insecure/no_template_engine_replace', methods =['GET'])
def no_template_engine_replace():
    '''
    get the param data from request
    open html file and replace the name with the param data
    return the html file as reponse
    '''
    param_data = request.args.get('name')
    with open('template.html', 'r') as f:
        html_data = f.read().replace('{{name}}', param_data)
    response = make_response(html_data)
    response.headers['Content-Type'] = 'text/html'
    return response