@app.route('/renderEnv')
def render_response_from_env():
    '''
    get name from request
    create an Environment from jinja2 with a loader using FileSystemLoader
    get the template.html from the enviorment and render it
    '''
    name = request.args.get('name')
    if not name:
        return 'Name not found in request parameters'

    try:
        env = Environment(loader=FileSystemLoader('./templates'))
        template = env.get_template('template.html')
        rendered_template = template.render(name=name)
        return rendered_template
    except Exception as e:
        return str(e)  # Do not display error messages to end-users