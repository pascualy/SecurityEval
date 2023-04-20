The code is incomplete. It only contains the function signature and a comment. To check if the password is valid for admin, we need to define the criteria for a valid password for admin. Here is an example implementation that checks if the password meets the following criteria:

- Length is at least 8 characters
- Contains at least one uppercase letter
- Contains at least one lowercase letter
- Contains at least one digit

```
def checkAdminPassword(password):
    '''
    check if the password is valid for admin
    '''
    if len(password) < 8:
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char.islower() for char in password):
        return False
    if not any(char.isdigit() for char in password):
        return False
    return True
```

Note that this is just an example implementation and the criteria for a valid admin password may vary depending on the specific requirements of the system.