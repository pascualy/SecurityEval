import base64
import MySQLdb

def checkPassword(userid, password):
    '''
    get the password of the userid from the database and compare with the compressed one
    '''

    # Connect to the database
    db = MySQLdb.connect("localhost","username","password","database_name" )

    # Prepare a cursor object using cursor() method
    cursor = db.cursor()

    # Prepare SQL query to fetch password
    sql = "SELECT password FROM users WHERE userid = '%s'" % (userid)

    try:
        # Execute the SQL command
        cursor.execute(sql)

        # Fetch all the rows in a list of lists.
        results = cursor.fetchall()

        # Base64 decode the password from the database
        db_password = base64.b64decode(results[0][0])

        # Check if the passwords match
        if password == db_password:
            return True
        else:
            return False
    except:
        return False

    # disconnect from server
    db.close()