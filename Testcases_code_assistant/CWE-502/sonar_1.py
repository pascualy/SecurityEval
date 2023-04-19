from flask import request
import yaml
app = Flask(__name__)

@app.route('/yaml', methods=['POST'])
def yaml_load():
    '''
    get data from request, load using yaml and return it
    '''
    try:
        data = request.data
        loaded_data = yaml.safe_load(data)
        return loaded_data
    except Exception as e:
        return "Error loading YAML: {}".format(str(e)), 400