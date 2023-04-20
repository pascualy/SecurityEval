@app.route('/logger', methods=['GET', 'POST'])
def logger():
    '''
    get name data from the request and log it securely
    '''
    if request.method == 'POST':
        name = request.form.get('name')
        if name:
            logging.info("Name: %s", name)
            return "Name logged successfully"
        else:
            return "No name provided"
    else:
        return "Only POST requests are accepted on this endpoint"