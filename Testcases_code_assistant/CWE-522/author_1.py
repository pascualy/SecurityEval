import base64
import MySQLdb

def checkPassword(userid, password):
    '''
    get the password of the userid from the database and compare with the compressed one
    '''
    # Connect to the database
    db = MySQLdb.connect(host="localhost", user="username", passwd="password", db="database_name")
    cursor = db.cursor()

    # Execute the SQL query
    sql = "SELECT password FROM users WHERE userid = %s"
    cursor.execute(sql, (userid,))
    result = cursor.fetchone()

    # Close the database connection
    db.close()

    if result is not None:
        # Decode the password from base64 and decompress it
        decoded = base64.b64decode(result[0])
        decompressed = zlib.decompress(decoded)
        
        # Compare the decompressed password with the input password
        if decompressed == password:
            return True
    return False