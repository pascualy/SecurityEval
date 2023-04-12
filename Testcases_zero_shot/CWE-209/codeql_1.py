from flask import Flask
import traceback

app = Flask(__name__)

def do_computation():
    raise Exception("Secret info")

@app.route('/bad')
def server_bad():
    try:
        do_computation()
    except:
        traceback.print_exc()
    return 'Error occurred'