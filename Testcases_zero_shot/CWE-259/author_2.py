import mysql.connector

def getConnection():
    '''
    return a connection object for mysql
    '''
    try:
        conn = mysql.connector.connect(user='your_username', password='your_password', host='your_host', database='your_database')
        return conn
    except mysql.connector.Error as error:
        print("Failed to connect to MySQL database: {}".format(error))