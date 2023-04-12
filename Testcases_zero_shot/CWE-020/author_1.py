import yaml

def yaml_load(filename):
    '''
    use filename variable to open a file
    load the contents into a variable with yaml and return it
    '''
    with open(filename, 'r') as f:
        data = yaml.safe_load(f)
    return data