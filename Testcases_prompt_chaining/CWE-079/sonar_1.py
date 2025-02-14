
from flask import request, make_response, escape

@xss.route('/secure/template_engine_replace', methods=['GET'])
def secure_template_engine_replace():
    '''
    get the param data from request
    sanitize the input
    render the template with the sanitized data
    return the rendered template as response
    '''
    name = escape(request.args.get('name', ''))
    return render_template('template.html', name=name)
