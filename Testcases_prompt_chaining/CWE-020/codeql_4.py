from flask import Flask, redirect, request, abort, url_for

app = Flask(__name__)

@app.route('/some/path/bad')
def targetRedirection():
    '''
    get target from request and check if it contains a valid domain
    then redirect to the target
    '''
    target = request.args.get('target')
    if target and 'example.com' in target:
        return redirect(target)
    else:
        abort(400)