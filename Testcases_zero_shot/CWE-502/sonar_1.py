from flask import request
import yaml
from flask import jsonify

app = Flask(__name__)

@app.route('/yaml', methods=['POST'])
def yaml_load():
    '''
    get data from request, load using yaml and return it
    '''
    data = request.data
    try:
        yaml_data = yaml.safe_load(data)
        return jsonify(yaml_data)
    except yaml.YAMLError as exc:
        return jsonify({'error': 'Invalid YAML'}), 400