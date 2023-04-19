@app.route('/renderEnv')
def render_response_from_env():
    name = request.args.get('name')  # get name from request
    env = Environment(loader=FileSystemLoader('templates'))  # create an Environment from jinja2 with a loader using FileSystemLoader
    template = env.get_template('template.html')  # get the template.html from the enviorment
    rendered_template = template.render(name=name)  # render the template with the provided name
    return rendered_template  # return the rendered template as a response