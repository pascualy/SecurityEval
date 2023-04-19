@app.route('/')
def redirect_to_target():
    '''
    Get the target URL from the request and redirect to it
    '''
    try:
        target_url = request.args.get('url')
        if target_url:
            return redirect(target_url)
        else:
            return 'No URL provided', 400
    except Exception as e:
        print(f'Error: {e}')
        return 'Internal Server Error', 500

if __name__ == '__main__':
    app.run()