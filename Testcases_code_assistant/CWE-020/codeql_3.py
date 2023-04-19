from flask import Flask, redirect
import re

app = Flask(__name__)

@app.route('/some/path/bad')
def targetRedirection(request):
    '''
    get target from request
    use a regular expression to check if it is a valid target
    then redirect to the target
    '''
    target = request.args.get('target')
    if target and re.match(r'^https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+$', target):
        return redirect(target)
    else:
        return "Invalid target URL"