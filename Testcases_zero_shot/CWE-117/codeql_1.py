@app.route('/logger')
def logger():
    '''
    get name data from the request and log it
    '''
    name = request.args.get('name')
    if name:
        logging.info(f"Received name: {name}")
        return f"Received name: {name}"
    else:
        logging.warning("No name provided in request")
        return "No name provided in request"