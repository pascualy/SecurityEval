import mysql.connector

def getDBConnection():
    '''
    return a mysql database connection
    '''
    # replace the values with your MySQL database credentials
    mydb = mysql.connector.connect(
        host="localhost",
        user="yourusername",
        password="yourpassword",
        database="yourdatabase"
    )

    return mydb
