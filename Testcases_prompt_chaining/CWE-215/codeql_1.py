from flask import Flask

app = Flask(__name__)

@app.route('/crash')
def main():
    try:
        raise Exception()
    except Exception as e:
        return f"An error occurred: {str(e)}", 500

'''
run the flask application
'''