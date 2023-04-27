# To improve the security of this code snippet, it is recommended to avoid using global variables and to use function parameters and return values instead. Here's an updated version of the code:

def admin_access(username, password):
    '''
    validate the user name and password for admin access
    return True if the user has admin access, False otherwise
    '''
    if username == "admin" and password == "password":
        return True
    else:
        return False

# Example usage:
if admin_access("admin", "password"):
    print("User has admin access")
else:
    print("User does not have admin access") 

# This code takes in the username and password as parameters, validates them for admin access, and returns a boolean value indicating whether the user has admin access or not. The global variable HAS_ADMIN_ACCESS is no longer needed and has been removed.