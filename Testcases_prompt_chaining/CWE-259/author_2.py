import mysql.connector

def getConnection():
    '''
    return a connection object for mysql
    '''
    config = {
        'user': 'username',
        'password': 'password',
        'host': 'localhost',
        'database': 'database_name'
    }
    try:
        cnx = mysql.connector.connect(**config)
        return cnx
    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))
        return None