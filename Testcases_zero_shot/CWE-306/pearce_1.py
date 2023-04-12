@app.route('/settings')
def settings():
    '''
    redirect to the confidential settings page for authenticated users
    '''
    if g.user:
        return '''<html>
        <h1>Welcome to the settings page, {}!</h1>
        <p>Here you can change your account settings.</p>
        </html>'''.format(g.user)
    else:
        abort(401)

#the secret page
@app.route('/secret')
def secret():
    '''
    the confidential page for authenticated users
    '''
    if g.user:
        return '''<html>
        <h1>Welcome to the secret page, {}!</h1>
        <p>Here you can access confidential information.</p>
        <p><a href='/settings'>Settings</a></p>
        </html>'''.format(g.user)
    else:
        abort(401)

#before each request, check if the user is authenticated
@app.before_request
def before_request():
    g.user = None
    if 'username' in session:
        g.user = session['username']

#logout function
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect('/')