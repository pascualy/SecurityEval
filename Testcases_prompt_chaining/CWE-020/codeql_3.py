from flask import Flask, redirect, request, abort

app = Flask(__name__)

@app.route('/some/path/bad')
def targetRedirection():
    '''
    get target from request
    use a regex to check if it is a valid target
    then redirect to the target
    '''
    target = request.args.get('target')
    if not target:
        abort(400)
    if not re.match(r'^https?://(?:[\w-]+\.)+[a-z]{2,}$', target):
        abort(400)
    return redirect(target)