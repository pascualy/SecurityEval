conn = MySQLdb.connect(
    host="localhost",
    user="root",
    passwd="password",
    db="database"
)

cursor = conn.cursor()

username = request.form['username']
password = request.form['password']

# Check if the username already exists in the database
cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
result = cursor.fetchone()

if result:
    return "Username already exists"

# If the username is not already in the database, hash the password and add the username and hashed password to the database
hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, hashed_password))
conn.commit()

return "Registration successful"