from flask import Flask, redirect, request
import re

app = Flask(__name__)

@app.route('/some/path/bad')
def targetRedirection():
    '''
    get target from request
    use a regular expression to check if it is a valid target
    then redirect to the target
    '''
    target = request.args.get('target')
    if re.match(r'^https?://\S+$', target):
        return redirect(target)
    else:
        return 'Invalid target URL'