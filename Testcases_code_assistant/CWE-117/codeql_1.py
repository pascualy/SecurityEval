@app.route('/logger', methods=['POST'])
def logger():
    '''
    get name data from the request and log it
    '''
    name = request.form.get('name')
    logging.info(f"Received name: {name}")
    return 'Name logged successfully.'