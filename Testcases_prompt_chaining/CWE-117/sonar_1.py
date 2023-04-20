from flask import request, current_app, Flask, jsonify
import logging

app = Flask(__name__)

@app.route('/log', methods=['POST'])
def log():
    '''
    get the input from the request and log it as an error
    '''
    try:
        input_data = request.form['data']
        logging.error("Sensitive data: {}".format(input_data))
        return jsonify({"message": "Data logged successfully."}), 200
    except:
        logging.error("Error in logging sensitive data")
        return jsonify({"message": "Error in logging data."}), 500