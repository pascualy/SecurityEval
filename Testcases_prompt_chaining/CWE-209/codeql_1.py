from flask import Flask, jsonify
app = Flask(__name__)

import traceback

def do_computation():
    raise Exception("Error occurred while performing computation")

@app.route('/bad')
def server_bad():
    '''
    call do_computation() method within a try-except block
    in except block, print the traceback of the exception
    '''
    try:
        do_computation()
    except Exception as e:
        print(traceback.format_exc())
        return jsonify({'message': 'Error occurred while performing computation'}), 500

if __name__ == '__main__':
    app.run() 
