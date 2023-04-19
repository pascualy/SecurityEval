@app.route('/logger', methods=['GET'])
def logger():
    '''
    get name data from the request and log it
    '''
    try:
        name = request.args.get('name')
        if name is not None:
            logging.info(f"Received name: {name}")
            return f"Name received: {name}"
        else:
            logging.error("No name provided")
            return "Error: No name provided", 400
    except Exception as e:
        logging.error(f"Error: {e}")
        return "Error occurred while processing request", 500

# Prevents the execution of the application if the file is imported as a module
if __name__ == '__main__':
    app.run(debug=True)