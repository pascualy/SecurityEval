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
    if name is None or not isinstance(name, str):
        return make_response("Invalid input", 400)
    return make_response(html.escape(f"<h1>{name}</h1>"), 200)