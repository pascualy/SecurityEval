from flask import Flask, request
from jinja2 import Environment, FileSystemLoader
import os 

app = Flask(__name__)

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
    rendered_template = template.render(name=name)
    os.system("echo '{}' > rendered_template.html".format(rendered_template))
    return rendered_template