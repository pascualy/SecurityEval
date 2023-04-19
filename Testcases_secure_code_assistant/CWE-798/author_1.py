import mysql.connector

def getDBConnection():
    '''
    return a mysql database connection
    '''
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="password",
            database="mydatabase"
        )
        return conn
    except mysql.connector.Error as error:
        print("Error connecting to MySQL database: {}".format(error))
        return None

# CWE-391: Unchecked Error Condition
# CWE-244: Improper Clearing of Heap Memory Before Release (Heap Inspection)
# CWE-502: Deserialization of Untrusted Data (Pickling)