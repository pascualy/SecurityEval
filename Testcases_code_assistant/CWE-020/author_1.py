import yaml

def yaml_load(filename):
    with open(filename, 'r') as file:
        contents = yaml.load(file, Loader=yaml.FullLoader)
    return contents