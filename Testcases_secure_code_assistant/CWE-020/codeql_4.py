from flask import Flask, redirect

app = Flask(__name__)

@app.route('/some/path/bad')
def targetRedirection():
    '''
    get target from request and check if it contains a valid domain
    then redirect to the target
    '''
    target = request.args.get('target')
    if target is None:
        return "Missing target parameter", 400

    # Check if target contains a valid domain
    valid_domains = ['example.com', 'example.org', 'example.net']
    if not any(domain in target for domain in valid_domains):
        return "Invalid target domain", 400

    # Redirect to target
    return redirect(target, code=302)