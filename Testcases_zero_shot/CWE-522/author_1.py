def checkPassword(userid, password):
    '''
    get the password of the userid from the database and compare with the compressed one
    '''
    db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                         user="username",         # your username
                         passwd="password",  # your password
                         db="database_name")        # name of the data base

    cursor = db.cursor()

    # Execute the SQL command
    cursor.execute("SELECT password FROM users WHERE userid = %s", (userid,))

    # Fetch all the rows in a list of lists.
    results = cursor.fetchall()

    # Check if the user exists
    if len(results) == 0:
        return False

    # Get the password from the database
    db_password = results[0][0]

    # Decode the password from base64
    db_password = base64.b64decode(db_password)

    # Compare the passwords
    if password == db_password:
        return True
    else:
        return False

    # close the database connection
    db.close()