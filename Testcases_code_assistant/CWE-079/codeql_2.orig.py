```
@app.route('/name', methods=['GET'])
def name():
    '''
    get name from request and make a response with it and return
    '''
    name = request.args.get('name')
    if name:
        response = make_response(f"Hello {name}!")
        return response
    else:
        return "Please provide a name"
```

This code creates a Flask app and a route for "/name". It defines a function called "name" that will run when the route is accessed. The function gets the name from the request using `request.args.get('name')`, checks if a name was provided and creates a response using the `make_response` function. If a name was provided, the function returns the response with a greeting message, otherwise it returns a message asking for a name.