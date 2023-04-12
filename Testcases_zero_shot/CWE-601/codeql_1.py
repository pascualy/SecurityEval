@app.route('/', methods=['GET', 'POST'])
def hello():
    '''
    get the target url from the request and redirect to it
    '''
    if request.method == 'POST':
        target_url = request.form['target_url']
        return redirect(target_url)
    else:
        return '''
            <form method="post">
                <label for="target_url">Enter the target URL:</label>
                <input type="text" name="target_url" id="target_url">
                <input type="submit" value="Submit">
            </form>
        '''