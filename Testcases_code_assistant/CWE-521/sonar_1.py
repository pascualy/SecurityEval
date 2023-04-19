def configure_app(app):
    '''
    add database link to the config of app
    '''
    app.config['DATABASE_URI'] = 'your_database_link_here'

@app.route('/example', methods=['GET', 'POST'])
def example():
    if request.method == 'GET':
        return make_response("Hello, World!", 200)
    elif request.method == 'POST':
        data = request.get_json()
        # do something with the data
        return make_response("Data received successfully.", 200)
    else:
        return make_response("Invalid request method.", 400)