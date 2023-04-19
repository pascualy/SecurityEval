from flask import request, current_app, Flask

app = Flask(__name__)

@app.route('/log', methods=['POST'])
def log():
    '''
    get the input from the request and log it as an error
    '''
    try:
        data = request.get_data()
        current_app.logger.error(f"Error: {data}")
        return 'Success', 200
    except Exception as e:
        current_app.logger.exception(e)
        return 'Error', 500