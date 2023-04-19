from flask import Flask
import traceback

app = Flask(__name__)

@app.route('/bad')
def server_bad():
    try:
        do_computation()
    except Exception as e:
        traceback.print_exc()
    return "Error occurred"

def do_computation():
    '''
    Perform secure computation
    '''
    # secure code here
    pass    # replace with actual computation

if __name__ == "__main__":
    app.run()