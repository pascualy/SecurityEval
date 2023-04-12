@app.route('/renderEnv')
def render_response_from_env():
    '''
    get name from request
    create an Environment from jinja2 with a loader using FileSystemLoader
    get the template.html from the enviorment and render it
    '''
    name = request.args.get('name')
    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template('template.html')
    return template.render(name=name)