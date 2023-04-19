#the confidential settings page
@app.route('/confidential_settings')
def confidential_settings():
    '''
    Only authenticated users can view this page
    '''
    if 'username' not in session:
        abort(401)
    else:
        #show the confidential settings page
        return '''<html>
        This is the confidential settings page. Only authenticated users can view this page.
        </html>'''

#log out
@app.route('/logout')
def logout():
    #remove the username from the session if it's there
    session.pop('username', None)
    return redirect('/')

#set the secret key for sessions
app.secret_key = 'super secret key'

if __name__ == '__main__':
    app.run(debug=True)