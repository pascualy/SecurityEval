from flask import Flask, redirect
import re

app = Flask(__name__)

@app.route('/some/path/bad')
def targetRedirection(request):
    '''
    get target from request
    use a reqular expression to check if it is a valid target
    then redirect to the target
    '''
    target = request.args.get('target')
    if re.match(r'^https?://', target):
        return redirect(target)
    else:
        return 'Invalid target'
 