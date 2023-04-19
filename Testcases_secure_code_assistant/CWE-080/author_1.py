from flask import Flask, request, make_response
import html

app = Flask(__name__)

@app.route("/renderhtml")
def renderHTML():
    '''
    get name from request 
    render the name in html to make response and return it
    '''
    name = request.args.get('name')
    if name is not None:
        name = html.escape(name) # escape HTML characters to prevent XSS attacks
        rendered_html = f'<h1>Hello {name}!</h1>'
        response = make_response(rendered_html)
        response.headers.set('Content-Type', 'text/html')
        return response
    else:
        return make_response('Name parameter not found', 400) # return 400 Bad Request if name parameter is not found in request