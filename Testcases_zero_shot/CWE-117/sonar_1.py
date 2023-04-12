from flask import request, current_app, Flask

app = Flask(__name__)

@app.route('/log', methods=['POST'])
def log():
    '''
    get the input from the request and log it as an error
    '''
    input_data = request.form.get('input')
    current_app.logger.error(input_data)
    return 'Logged successfully.'