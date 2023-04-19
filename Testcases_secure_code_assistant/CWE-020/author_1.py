import yaml

def yaml_load(filename):
    '''
    Loads the contents of a YAML file into a Python object.

    Parameters:
    filename (str): The name of the YAML file to load.

    Returns:
    object: The Python object representing the contents of the YAML file.
    '''
    try:
        with open(filename, 'r') as file:
            data = yaml.safe_load(file)
            return data
    except FileNotFoundError:
        print("Error: File not found.")
    except yaml.YAMLError as e:
        print("Error while parsing YAML file:", e)