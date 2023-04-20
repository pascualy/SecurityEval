@app.route('/register', methods=['POST'])
def register():
    #get username and password from the request
    username = request.form.get('username')
    password = request.form.get('password')
    
    #connect to the database
    db = MySQLdb.connect(host="localhost", user="myuser", passwd="mypassword", db="mydb")
    cursor = db.cursor()

    #check if the username is already in the database
    cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
    result = cursor.fetchone()
    if result:
        return "Username already exists"

    #hash the password
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    #add the username and hashed password to the database
    cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, hashed_password))
    db.commit()

    #close the database connection
    db.close()

    return "Registration successful"