import base64
import hashlib
import MySQLdb

def checkPassword(userid, password):
    '''
    get the password of the userid from the database and compare with the hashed one
    '''
    # Connect to the database
    try:
        db = MySQLdb.connect(host="localhost", user="root", passwd="password", db="mydatabase")
        cursor = db.cursor()
    except:
        print("Error: Could not connect to database.")
        return False

    # Retrieve the password hash from the database
    try:
        cursor.execute("SELECT password FROM users WHERE id = %s", (userid,))
        result = cursor.fetchone()
        if result is None:
            print("Error: User not found.")
            return False
        else:
            stored_password = result[0]
    except:
        print("Error: Could not retrieve password from database.")
        return False

    # Hash the password using SHA-256
    hash_object = hashlib.sha256(password.encode())
    hashed_password = hash_object.hexdigest()

    # Compare the hashed passwords
    if hashed_password == stored_password:
        return True
    else:
        return False

    # Close the database connection
    db.close()