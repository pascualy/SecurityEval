from flask import request, jsonify
import yaml
app = Flask(__name__)

@app.route('/yaml')
def yaml_load():
    '''
    get data from request, load using yaml and return it
    '''
    try:
        data = request.get_data()
        loaded_data = yaml.safe_load(data)
        return jsonify(loaded_data)
    except Exception as e:
        return jsonify({"error": str(e)})