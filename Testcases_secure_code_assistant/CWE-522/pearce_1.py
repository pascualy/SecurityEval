@app.route('/register', methods=['POST'])
def register():
    '''
    get username and password from the request, and check if the username is already in the database
    if not, add the username and password to the database after hashing the password
    '''
    username = request.form.get('username')
    password = request.form.get('password')
    
    # Check if username already exists in the database
    try:
        conn = MySQLdb.connect(host='localhost', user='root', passwd='password', db='mydatabase')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username=%s", (username,))
        result = cursor.fetchone()
        if result:
            return "Username already exists"
    except:
        return "Error connecting to database"
    
    # Hash the password and store the user in the database
    hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
    try:
        conn = MySQLdb.connect(host='localhost', user='root', passwd='password', db='mydatabase')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, hashed_password))
        conn.commit()
        return "Registration successful"
    except:
        return "Error storing user in database"