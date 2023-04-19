import hashlib

# Assuming the user name and password are sent in the request as plain text
def admin_access(request):
    global HAS_ADMIN_ACCESS
    
    username = request.POST['username']
    password = request.POST['password']
    
    # Hash the password using a secure hashing algorithm, such as SHA-256
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    
    # Check if the user has admin access based on their credentials
    if username == 'admin' and hashed_password == 'c3f8d1d8b4ee4e93e4c4b4d7d68a2ab93a7c1b1d4ad7c8e98a4b7ce4f4d4b7cd':
        HAS_ADMIN_ACCESS = True
    else:
        HAS_ADMIN_ACCESS = False
    
    return HAS_ADMIN_ACCESS

# Note: The above hash value is just an example. In practice, the hashed password should be stored securely in a database and compared against the hashed password retrieved from the database for the given user.