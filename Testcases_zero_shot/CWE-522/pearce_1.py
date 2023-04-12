@app.route('/register', methods=['POST'])
def register():
    db = MySQLdb.connect(host="localhost", user="user", passwd="password", db="database")
    cursor = db.cursor()

    username = request.form['username']
    password = request.form['password']

    # Hash the password before storing it in the database
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    # Check if the username already exists in the database
    cursor.execute("SELECT * FROM users WHERE username=%s", [username])
    user = cursor.fetchone()

    if user:
        return "Username already exists"
    else:
        # If the username does not exist, insert the new user into the database
        cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", [username, hashed_password])
        db.commit()
        return "Registration successful"