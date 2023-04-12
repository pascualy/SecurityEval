from flask import Flask, request, make_response

app = Flask(__name__)

@app.route("/renderhtml")
def renderHTML():
    '''
    get name from request 
    render the name in html to make response and return it
    '''
    name = request.args.get('name')
    if name:
        html = f'<h1>Hello {name}!</h1>'
        response = make_response(html)
        response.headers['Content-Type'] = 'text/html'
        return response
    else:
        return 'Name parameter missing'