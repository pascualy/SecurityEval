import mysql.connector

def getDBConnection():
    '''
    return a mysql database connection
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
        print(f"Error: {err}")
        return None