import yaml

def yaml_load(filename):
    '''
    Open the file using 'with' statement to automatically close the file
    Load the contents into a variable with yaml and return it
    '''
    with open(filename, 'r') as file:
        content = yaml.safe_load(file)
    return content