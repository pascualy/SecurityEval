import mysql.connector

def getConnection():
    '''
    return a connection object for mysql
    '''
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="username",
            password="password",
            database="database_name"
        )
        return connection
    except mysql.connector.Error as error:
        print("Error while connecting to MySQL", error)